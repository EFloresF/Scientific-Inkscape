#!/usr/bin/env python
# coding=utf-8
#
# Copyright (c) 2020 David Burghoff <dburghoff@nd.edu>
#
# Functions modified from Inkex were made by
#                    Martin Owens <doctormo@gmail.com>
#                    Sergei Izmailov <sergei.a.izmailov@gmail.com>
#                    Thomas Holder <thomas.holder@schrodinger.com>
#                    Jonathan Neuhauser <jonathan.neuhauser@outlook.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

""" Patches for speeding up native Inkex functions after import """
import inkex
from inkex import Transform
import re, inspect, lxml
import Style0  # since this modifies inkex.BaseElement.WRAPPED_ATTRS

""" _base.py """
# Inkex's get does a lot of namespace adding that can be cached for speed
# This can be bypassed altogether for known attributes (by using fget instead)
fget = lxml.etree.ElementBase.get;
fset = lxml.etree.ElementBase.set;

wrapped_props = {row[0]: (row[-2], row[-1]) for row in inkex.BaseElement.WRAPPED_ATTRS}
wrapped_props_keys = set(wrapped_props.keys())
wrapped_attrs =  {row[-2]: (row[0], row[-1]) for row in inkex.BaseElement.WRAPPED_ATTRS}
wrapped_attrs_keys = set(wrapped_attrs.keys())
NSatts,wrprops = dict(), dict()      
inkexget = inkex.BaseElement.get;
def fast_get(self, attr, default=None):
    try:
        return fget(self,NSatts[attr], default)
    except:
        try:
            value = getattr(self, wrprops[attr], None)
            ret = str(value) if value else (default or None)
            return ret
        except:
            if attr in wrapped_attrs_keys:
                (wrprops[attr], _) = wrapped_attrs[attr]
            else:
                NSatts[attr] = inkex.addNS(attr)
            return inkexget(self, attr, default)
inkex.BaseElement.get = fast_get

def fast_set(self, attr, value):
    """Set element attribute named, with addNS support"""
    if attr in wrapped_attrs:
        # Always keep the local wrapped class up to date.
        (prop, cls) = wrapped_attrs[attr]
        setattr(self, prop, cls(value))
        value = getattr(self, prop)
        if not value:
            return 
    try:
        NSattr = NSatts[attr]
    except:
        NSatts[attr] = inkex.addNS(attr)
        NSattr = NSatts[attr]
        
    if value is None:
        self.attrib.pop(NSattr, None)  # pylint: disable=no-member
    else:
        value = str(value)
        fset(self,NSattr, value)
inkex.BaseElement.set = fast_set

def fast_getattr(self, name):
    """Get the attribute, but load it if it is not available yet"""
    # if name in wrapped_props_keys:   # always satisfied
    (attr, cls) = wrapped_props[name]
    def _set_attr(new_item):
        if new_item:
            self.set(attr, str(new_item))
        else:
            self.attrib.pop(attr, None)  # pylint: disable=no-member

    # pylint: disable=no-member
    value = cls(self.attrib.get(attr, None), callback=_set_attr)
    if name == "style":
        value.element = self
    fast_setattr(self, name, value)
    return value
    # raise AttributeError(f"Can't find attribute {self.typename}.{name}")

def fast_setattr(self, name, value):
    """Set the attribute, update it if needed"""
    # if name in wrapped_props_keys:   # always satisfied
    (attr, cls) = wrapped_props[name]
    # Don't call self.set or self.get (infinate loop)
    if value:
        if not isinstance(value, cls):
            value = cls(value)
        self.attrib[attr] = str(value)
    else:
        self.attrib.pop(attr, None)  # pylint: disable=no-member

# _base.py overloads __setattr__ and __getattr__, which adds a lot of overhead
# since they're invoked for all class attributes, not just transform etc.
# We remove the overloading and replicate it using properties. Since there
# are only a few attributes to overload, this is fine.
del inkex.BaseElement.__setattr__
del inkex.BaseElement.__getattr__
for prop in wrapped_props_keys:
    get_func = lambda self, attr=prop: fast_getattr(self, attr)
    set_func = lambda self, value, attr=prop: fast_setattr(self, attr, value)
    setattr(inkex.BaseElement, prop, property(get_func, set_func))




""" paths.py """
# A faster version of Vector2d that only allows for 2 input args
V2d = inkex.transforms.Vector2d
class Vector2da(V2d):
    __slots__ = ('_x', '_y') # preallocation speeds
    def __init__(self,x,y):
        self._x = float(x);
        self._y = float(y);
def line_move_arc_end_point(self, first, prev):
    return Vector2da(self.x, self.y)
def horz_end_point(self, first, prev):
    return Vector2da(self.x, prev.y)
def vert_end_point(self, first, prev):
    return Vector2da(prev.x, self.y)
def curve_smooth_end_point(self, first, prev):
    return Vector2da(self.x4, self.y4)
def quadratic_tepid_quadratic_end_point(self, first, prev):
    return Vector2da(self.x3, self.y3)
inkex.paths.Line.end_point = line_move_arc_end_point
inkex.paths.Move.end_point = line_move_arc_end_point
inkex.paths.Arc.end_point = line_move_arc_end_point
inkex.paths.Horz.end_point = horz_end_point
inkex.paths.Vert.end_point = vert_end_point
inkex.paths.Curve.end_point = curve_smooth_end_point
inkex.paths.Smooth.end_point = curve_smooth_end_point
inkex.paths.Quadratic.end_point = quadratic_tepid_quadratic_end_point
inkex.paths.TepidQuadratic.end_point = quadratic_tepid_quadratic_end_point


# A version of end_points that avoids unnecessary instance checks
zZmM = {'z','Z','m','M'}
def fast_end_points(self):
    prev = Vector2da(0,0)
    first = Vector2da(0,0)
    for seg in self:  
        end_point = seg.end_point(first, prev)
        if seg.letter in zZmM:
            first = end_point
        prev = end_point
        yield end_point
inkex.paths.Path.end_points = property(fast_end_points)


# Optimize Path's init to avoid calls to append and reduce instance checks
# About 50% faster
ipcspth, ipln = inkex.paths.CubicSuperPath, inkex.paths.Line
ipPC = inkex.paths.PathCommand
PCsubs = set(); # precache all types that are instances of PathCommand
for _, obj in inspect.getmembers(inkex.paths):
    if inspect.isclass(obj) and issubclass(obj, ipPC):
        PCsubs.add(obj)
def process_items(items):
    for item in items:
        # if isinstance(item, ipPC):
        itemtype = type(item)
        if itemtype in PCsubs:
            yield item  
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            if isinstance(item[1], (list, tuple)):
                yield ipPC.letter_to_class(item[0])(*item[1])
            else:
                yield ipln(*item)
        else:
            raise TypeError(
                f"Bad path type: {type(items).__name__}"
                f"({type(item).__name__}, ...): {item}"
            )
def fast_init(self, path_d=None):
    list.__init__(self)
    if isinstance(path_d, str):
        # Returns a generator returning PathCommand objects
        path_d = self.parse_string(path_d)
        self.extend(path_d)
    else:
        if isinstance(path_d, ipcspth):
            path_d = path_d.to_path()
        self.extend(process_items(path_d or ()))
inkex.paths.Path.__init__ = fast_init

# Cache PathCommand letters and remove property
letts = dict()
for pc in PCsubs:
    letts[pc]=pc.letter
del ipPC.letter
for pc in PCsubs:
    pc.letter = letts[pc]

# Make parse_string faster by combining with strargs (about 20% faster)
LEX_REX = inkex.paths.LEX_REX
try:
    NUMBER_REX = inkex.utils.NUMBER_REX
except:
    DIGIT_REX_PART = r"[0-9]"
    DIGIT_SEQUENCE_REX_PART = rf"(?:{DIGIT_REX_PART}+)"
    INTEGER_CONSTANT_REX_PART = DIGIT_SEQUENCE_REX_PART
    SIGN_REX_PART = r"[+-]"
    EXPONENT_REX_PART = rf"(?:[eE]{SIGN_REX_PART}?{DIGIT_SEQUENCE_REX_PART})"
    FRACTIONAL_CONSTANT_REX_PART = rf"(?:{DIGIT_SEQUENCE_REX_PART}?\.{DIGIT_SEQUENCE_REX_PART}|{DIGIT_SEQUENCE_REX_PART}\.)"
    FLOATING_POINT_CONSTANT_REX_PART = rf"(?:{FRACTIONAL_CONSTANT_REX_PART}{EXPONENT_REX_PART}?|{DIGIT_SEQUENCE_REX_PART}{EXPONENT_REX_PART})"
    NUMBER_REX = re.compile(
        rf"(?:{SIGN_REX_PART}?{FLOATING_POINT_CONSTANT_REX_PART}|{SIGN_REX_PART}?{INTEGER_CONSTANT_REX_PART})"
    )
letter_to_class = ipPC._letter_to_class
nargs_cache = {cmd: cmd.nargs for cmd in letter_to_class.values()}
next_command_cache = {cmd: cmd.next_command for cmd in letter_to_class.values()}
# inkex.utils.debug(next_command_cache)
def fast_parse_string(cls, path_d):
    for cmd, numbers in LEX_REX.findall(path_d):
        args = [float(val) for val in NUMBER_REX.findall(numbers)]
        cmd = letter_to_class[cmd]
        cmd_nargs = nargs_cache[cmd]
        i = 0
        args_len = len(args)
        while i < args_len or cmd_nargs == 0:
            if args_len < i + cmd_nargs:
                return
            seg = cmd(*args[i: i + cmd_nargs])
            i += cmd_nargs
            # cmd = seg.next_command
            cmd = next_command_cache[type(seg)]
            cmd_nargs = nargs_cache[cmd]
            yield seg
inkex.paths.Path.parse_string = fast_parse_string





""" transforms.py """
# Faster apply_to_point that gets rid of property calls
def apply_to_point_mod(obj, pt, simple=False):
    ptx, pty = pt if isinstance(pt, (tuple, list)) else (pt.x, pt.y)
    x = obj.matrix[0][0] * ptx + obj.matrix[0][1] * pty + obj.matrix[0][2]
    y = obj.matrix[1][0] * ptx + obj.matrix[1][1] * pty + obj.matrix[1][2]
    return Vector2da(x, y)
old_atp = inkex.Transform.apply_to_point
inkex.Transform.apply_to_point = apply_to_point_mod

# Applies inverse of transform to point without making a new Transform
def applyI_to_point(obj, pt):
    m = obj.matrix
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    inv_det = 1 / det
    sx = pt.x - m[0][2]  # pt.x is sometimes a numpy float64?
    sy = pt.y - m[1][2]
    x = (m[1][1] * sx - m[0][1] * sy) * inv_det
    y = (m[0][0] * sy - m[1][0] * sx) * inv_det
    return Vector2da(x, y)
inkex.Transform.applyI_to_point = applyI_to_point

 # Built-in bool initializes multiple Transforms
Itmat = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0))
def Tbool(obj):
    return obj.matrix!=Itmat     # exact, not within tolerance. I think this is fine
inkex.Transform.__bool__ = Tbool

# Reduce Transform conversions during transform multiplication
def matmul2(obj, matrix):
    if isinstance(matrix, (Transform)):
        othermat = matrix.matrix
    elif isinstance(matrix, (tuple)):
        othermat = matrix
    else:
        othermat = Transform(matrix).matrix
        # I think this is never called
    return Transform(
        (
            obj.matrix[0][0] * othermat[0][0] + obj.matrix[0][1] * othermat[1][0],
            obj.matrix[1][0] * othermat[0][0] + obj.matrix[1][1] * othermat[1][0],
            obj.matrix[0][0] * othermat[0][1] + obj.matrix[0][1] * othermat[1][1],
            obj.matrix[1][0] * othermat[0][1] + obj.matrix[1][1] * othermat[1][1],
            obj.matrix[0][0] * othermat[0][2]
            + obj.matrix[0][1] * othermat[1][2]
            + obj.matrix[0][2],
            obj.matrix[1][0] * othermat[0][2]
            + obj.matrix[1][1] * othermat[1][2]
            + obj.matrix[1][2],
        )
    )
inkex.transforms.Transform.__matmul__ = matmul2
def imatmul2(self, othermat):
    if isinstance(othermat, (Transform)):
        othermat = othermat.matrix
    self.matrix = (
        (self.matrix[0][0] * othermat[0][0] + self.matrix[0][1] * othermat[1][0],
         self.matrix[0][0] * othermat[0][1] + self.matrix[0][1] * othermat[1][1],
         self.matrix[0][0] * othermat[0][2] + self.matrix[0][1] * othermat[1][2] + self.matrix[0][2]),
        (self.matrix[1][0] * othermat[0][0] + self.matrix[1][1] * othermat[1][0],
         self.matrix[1][0] * othermat[0][1] + self.matrix[1][1] * othermat[1][1],
         self.matrix[1][0] * othermat[0][2] + self.matrix[1][1] * othermat[1][2] + self.matrix[1][2])
    )
    if self.callback is not None:
        self.callback(self)
    return self
inkex.transforms.Transform.__imatmul__ = imatmul2

# Rewrite ImmutableVector2d since 2 arguments most common
IV2d = inkex.transforms.ImmutableVector2d
def IV2d_init(self, *args, fallback=None):
    try:
        self._x, self._y = map(float, args)
    except:
        try:
            if len(args) == 0:
                x, y = 0.0, 0.0
            elif len(args) == 1:
                x, y = self._parse(args[0])
            else:
                raise ValueError("too many arguments")
        except (ValueError, TypeError) as error:
            if fallback is None:
                raise ValueError("Cannot parse vector and no fallback given") from error
            x, y = IV2d(fallback)
        self._x, self._y = float(x), float(y)
inkex.transforms.ImmutableVector2d.__init__ = IV2d_init


