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
# Functions modified from Deep_Ungroup made by Nikita Kitaev
#
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



import inkex
from inkex import (
    TextElement, FlowRoot, FlowPara, FlowSpan, Tspan, TextPath, Rectangle, \
        addNS, Transform, ClipPath, Use, NamedView, Defs, \
        Metadata, ForeignObject, Vector2d, Path, Line, PathElement,command,\
        SvgDocumentElement,Image,Group,Polyline,Anchor,Switch,ShapeElement, BaseElement,FlowRegion)
from applytransform_mod import ApplyTransform
import lxml, math
from lxml import etree  
from Style2 import Style2


import copy
def descendants2(el,return_tails=False):
    # Like Inkex's descendants(), but avoids recursion to avoid recursion depth issues
    cel = el;
    keepgoing = True; childrendone = False;
    descendants = [];
    precedingtails = [];
    
    # To avoid repeated lookups of each element's children and index, make dicts
    # that store them once they've been looked up
    children_dict = dict();
    parent_dict   = dict();
    index_dict = dict();
    pendingtails = [];
    def getchildren_dict(eli):
        if not(eli in children_dict):
            children_dict[eli] = list(eli)               # getchildren deprecated
            for ii in range(len(children_dict[eli])):
                index_dict[children_dict[eli][ii]] = ii; # store index for later
        return children_dict[eli]
    def myindex(eli):   # index amongst siblings
        if not(eli in index_dict):
            index_dict[eli] = getchildren_dict(getparent_dict(eli)).index(eli); # shouldn't need, just in case
        return index_dict[eli]
    def getparent_dict(eli):
        if not(eli in parent_dict):
            parent_dict[eli] = eli.getparent()               
        return parent_dict[eli]
        
    
    while keepgoing:
        keepgoing = False;
        if not(childrendone):
            descendants.append(cel);
            precedingtails.append(copy.copy(pendingtails))
            pendingtails = [];

            ks = getchildren_dict(cel);
            if len(ks)>0: # try children
                cel = ks[0];
                keepgoing = True; childrendone = False; continue;
            else:
                pendingtails.append(cel);
        
        if cel==el:
            keepgoing = False; continue;   # we're finished
        else:
            par  = getparent_dict(cel);
            sibs = getchildren_dict(par)
            myi = myindex(cel)
            if myi!=len(sibs)-1: # try younger siblings
                cel = sibs[myi+1];
                keepgoing = True; childrendone = False; continue;
            else:
                cel = par;
                pendingtails.append(cel); 
                keepgoing = True; childrendone = True; continue;
    descendants = [v for v in descendants if isinstance(v, (BaseElement, str))]
    
    if not(return_tails):
        return descendants;
    else:
        # For each descendants return a list of what element we expect our tails to precede
        precedingtails.append(pendingtails);  # will be one longer than descendants because of the last one
        return descendants, precedingtails, children_dict, parent_dict

# Sets a style property  
def Set_Style_Comp(el_or_sty,comp,val):
    isel = isinstance(el_or_sty,(BaseElement))  # is element
    if isel:
        sty = el_or_sty.get('style');
    else:
        isstr = isinstance(el_or_sty,(str))
        if not(isstr):                          # is style string
            sty = str(el_or_sty)
        else:                                   # is Style element
            sty = el_or_sty

    if sty is not None:
        sty = sty.split(';');
        compfound=False;
        for ii in range(len(sty)):
            if comp in sty[ii]:
                if val is not None:
                    sty[ii] = comp+':'+val;
                else:
                    sty[ii] = ''
                compfound=True;
        if not(compfound):
            if val is not None:
                sty.append(comp+':'+val);
            else: pass
        sty = [v.strip(';') for v in sty if v!=''];
        sty = ';'.join(sty)
    else:
        if val is not None:
            sty = comp+':'+val
    
    if isel:
        el_or_sty.set('style',sty);             # set element style
    else:
        if isstr:
            return sty                          # return style string
        else:
            return Style2(sty)                  # convert back to Style
    

# gets a style property (return None if none)
def Get_Style_Comp(sty,comp):
    sty=str(sty);
    val=None;
    if sty is not None:
        sty = sty.split(';');
        for ii in range(len(sty)):
            a=sty[ii].split(':');
            if comp.lower()==a[0].lower():
                val=a[1];
    return val

# A temporary version of the new selected_style until it's officially released.
# Maybe replace later (but it's currently way faster, so maybe not)
def selected_style_local(el):
    parent = el.getparent();
    if parent is not None and isinstance(parent, (ShapeElement,SvgDocumentElement)):
        return selected_style_local(parent) + cascaded_style2(el) 
    return cascaded_style2(el)

svgpres = ['alignment-baseline','baseline-shift','clip','clip-path','clip-rule','color','color-interpolation','color-interpolation-filters','color-profile','color-rendering','cursor','direction','display','dominant-baseline','enable-background','fill','fill-opacity','fill-rule','filter','flood-color','flood-opacity','font-family','font-size','font-size-adjust','font-stretch','font-style','font-variant','font-weight','glyph-orientation-horizontal','glyph-orientation-vertical','image-rendering','kerning','letter-spacing','lighting-color','marker-end','marker-mid','marker-start','mask','opacity','overflow','pointer-events','shape-rendering','stop-color','stop-opacity','stroke','stroke-dasharray','stroke-dashoffset','stroke-linecap','stroke-linejoin','stroke-miterlimit','stroke-opacity','stroke-width','text-anchor','text-decoration','text-rendering','transform','transform-origin','unicode-bidi','vector-effect','visibility','word-spacing','writing-mode']
excludes = ['clip','clip-path','mask','transform','transform-origin']
global cssdict
cssdict = None;
def cascaded_style2(el):
# Object's style including any CSS
# Modified from Inkex's cascaded_style
    global cssdict
    if cssdict is None:
        # Generate a dictionary of styles at least once so we don't have to do constant lookups
        # If elements change, will need to rerun by setting cssdict to None
        generate_cssdict(get_parent_svg(el));
    csssty = cssdict.get(el.get_id());
    # idebug(csssty)
    # locsty = el.style;
    locsty = Style2(el.get('style'));
    
    # Add any presentation attributes to local style
    attr = list(el.keys());
    attsty = Style2('');
    for a in attr:
        if a in svgpres and not(a in excludes) and locsty.get(a) is None and el.get(a) is not None:
            attsty[a] = el.get(a)
#            debug(el.get(a))

    if csssty is None:
        return attsty+locsty
    else:
        # Any style specified locally takes priority, followed by CSS,
        # followed by any attributes that the element has
        return attsty+csssty+locsty
def dupe_in_cssdict(oldid,newid):
    # duplicate a style in cssdict
    global cssdict
    if cssdict is not None:
        csssty = cssdict.get(oldid);
        if csssty is not None:
            cssdict[newid]=csssty;
def generate_cssdict(svg):
    global cssdict
    cssdict= dict();
    for sheet in svg.root.stylesheets:
        for style in sheet:
            try:
                # els = svg.xpath(style.to_xpath())
                els = svg.xpath(vto_xpath(style))
                for elem in els:
                    elid = elem.get('id',None);
                    # idebug(elid)
                    if elid is not None and style!=inkex.Style():  # still using Inkex's Style here since from stylesheets
                        if cssdict.get(elid) is None:
                            cssdict[elid] = Style2() + style;
                        else:
                            cssdict[elid] += style;
            except (lxml.etree.XPathEvalError,TypeError):
                pass
            
    
# For style components that represent a size (stroke-width, font-size, etc), calculate
# the true size reported by Inkscape in user units, inheriting any styles/transforms/document scaling
def Get_Composed_Width(el,comp,nargout=1,styin=None,ctin=None):
    # cs = el.composed_style();
    if styin is None:                   # can pass styin to reduce extra style gets
        cs = selected_style_local(el);
    else:
        cs = styin;
    if ctin is None:                    # can pass ctin to reduce extra composed_transforms
        ct = el.composed_transform();
    else:
        ct = ctin;
    if nargout==4:
        ang = math.atan2(ct.c,ct.d)*180/math.pi;
    svg = get_parent_svg(el)
    docscale = 1;
    if svg is not None:
        docscale = vscale(svg);
    sc = Get_Style_Comp(cs,comp);
    # debug(sc)
    if sc is not None:
        if '%' in sc: # relative width, get parent width
            sc = float(sc.strip('%'))/100;
            fs, sf, ct, ang = Get_Composed_Width(el.getparent(),comp,4)
            if nargout==4:
                ang = math.atan2(ct.c,ct.d)*180/math.pi;
                return fs*sc,sf,ct,ang
            else:
                return fs*sc
        else:
            sw = implicitpx(sc)
            sf = math.sqrt(abs(ct.a*ct.d - ct.b*ct.c))*docscale # scale factor
            if nargout==4:
                return sw*sf, sf, ct, ang
            else:
                return sw*sf
    else:
        if comp=='font-size':
            sf = math.sqrt(abs(ct.a*ct.d - ct.b*ct.c))*docscale # scale factor
            returnval = 12*sf; # default font is 12 uu
        else:
            returnval = None;
            sf = None;
            
        if nargout==4:
            return returnval,sf,ct,ang
        else:
            return returnval
    
# Get line-height in user units
def Get_Composed_LineHeight(el,styin=None,ctin=None):    # cs = el.composed_style();
    if styin is None:
        cs = selected_style_local(el);
    else:
        cs = styin;
    sc = Get_Style_Comp(cs,'line-height');
    if sc is not None:
        if '%' in sc: # relative width, get parent width
            sc = float(sc.strip('%'))/100;
        elif sc.lower()=='normal':
            sc = 1.25
        else:
            sc = float(sc);
    if sc is None:
        sc = 1.25;   # default line-height is 12 uu
    fs = Get_Composed_Width(el,'font-size',styin=styin,ctin=ctin)
    return sc*fs
    
# For style components that are a list (stroke-dasharray), calculate
# the true size reported by Inkscape, inheriting any styles/transforms
def Get_Composed_List(el,comp,nargout=1,styin=None):
    # cs = el.composed_style();
    if styin is None:
        cs = selected_style_local(el);
    else:
        cs = styin
    ct = el.composed_transform();
    sc = Get_Style_Comp(cs,comp);
    svg = get_parent_svg(el);
    docscale = 1;
    if svg is not None:
        docscale = vscale(svg);
    if sc=='none':
        return 'none'
    elif sc is not None:
        sw = sc.split(',')
        # sw = sc.strip().replace("px", "").split(',')
        sf = math.sqrt(abs(ct.a*ct.d - ct.b*ct.c))*docscale
        sw = [implicitpx(x)*sf for x in sw];
        if nargout==1:
            return sw
        else:
            return sw,sf
    else:
        if nargout==1:
            return None
        else:
            return None, None

# Unit parser and renderer
def uparse(str):
    if str is not None:
        uv = inkex.units.parse_unit(str,default_unit=None);
        return uv[0],uv[1]
    else:
        return None, None
def urender(v,u):
    if v is not None:
        if u is not None:
            return inkex.units.render_unit(v,u);
        else:
            return str(v)
    else:
        return None
    
def implicitpx(strin):
    # For many properties, a size specification of '1px' actually means '1uu'
    # Even if the size explicitly says '1mm' and the user units are mm, this will be
    # first converted to px and then interpreted to mean user units. (So '1mm' would
    # up being bigger than 1 mm). This returns the size as Inkscape will interpret it (in uu)
    if strin is None:
        return None
    else:
        return inkex.units.convert_unit(strin.lower().strip(), 'px');
#    return inkex.units.convert_unit(str.lower().strip(), 'px', default='px') # fails pre-1.1, default is px anyway
        

# Get points of a path, element, or rectangle in the global coordinate system
def get_points(el,irange=None):
    # if isinstance(el,Line): #el.typename=='Line':
    #     pts = [Vector2d(el.get('x1'),el.get('y1')),\
    #            Vector2d(el.get('x2'),el.get('y2'))];
    # elif isinstance(el,(PathElement,Polyline)): # el.typename=='PathElement':
    #     pth=Path(el.get_path()).to_absolute();
    #     if irange is not None:
    #         pnew = Path();
    #         for ii in range(irange[0],irange[1]):
    #             pnew.append(pth[ii])
    #         pth = pnew
    #     pts = list(pth.control_points);
    # elif isinstance(el,Rectangle):  # el.typename=='Rectangle':
    #     x = (el.get('x'));
    #     y = (el.get('y'));
    #     w = (el.get('width'));
    #     h = (el.get('height'));
    #     if x is not None and y is not None and w is not None and h is not None:
    #         x = float(x);
    #         y = float(y);
    #         w = float(w);
    #         h = float(h);
    #         pts = [Vector2d(x,y),Vector2d(x+w,y),Vector2d(x+w,y+h),Vector2d(x,y+h),Vector2d(x,y)];
    #     else:
    #         pts = [];
    pth=Path(get_path2(el)).to_absolute();
    if irange is not None:
        pnew = Path();
        for ii in range(irange[0],irange[1]):
            pnew.append(pth[ii])
        pth = pnew
    pts = list(pth.end_points);
            
    ct = el.composed_transform();
    
    mysvg = get_parent_svg(el);
    docscale = 1;
    if mysvg is not None:
        docscale = vscale(mysvg);
        
    xs = []; ys = [];
    for p in pts:
        p = ct.apply_to_point(p);
        xs.append(p.x*docscale)
        ys.append(p.y*docscale)
    return xs, ys

# def isRectanglePath(el):
#     isrect = False;
#     if isinstance(el,(PathElement,Rectangle,Line,Polyline)): 
#         xs, ys = get_points(el);
        
#         if 3<=len(xs)<=5 and len(set(xs))==2 and len(set(ys))==2:
#             isrect = True;
#     return isrect

# Unlinks clones and composes transform/clips/etc, along with descendants
def unlink2(el):
    if isinstance(el,(Use)):
        useid = el.get('xlink:href');
        useel = getElementById2(get_parent_svg(el),useid[1:]);
        if useel is not None:         
            d = duplicate2(useel)

            # xy translation treated as a transform (applied first, then clip/mask, then full xform)
            tx = el.get('x'); ty=el.get('y')
            if tx is None: tx = 0;
            if ty is None: ty = 0;
            # order: x,y translation, then clip/mask, then transform
            compose_all(d,None,None,Transform('translate('+str(tx)+','+str(ty)+')'),None)
            compose_all(d,el.get('clip-path'),el.get('mask'),Transform(el.get('transform')),cascaded_style2(el))
            replace_element(el, d);
            d.set('unlinked_clone',True);
            for k in descendants2(d)[1:]:
                unlink2(k)
            return d
        else:
            return el
    else:
        return el
    
unungroupable = (NamedView, Defs, Metadata, ForeignObject, lxml.etree._Comment)
def ungroup(groupnode):
    # Pops a node out of its group, unless it's already in a layer or the base
    # Unlink any clones that aren't glyphs
    # Remove any comments, Preserves style, clipping, and masking
    
    gparent = groupnode.getparent()
    gindex  = list(gparent).index(groupnode)   # group's location in parent
    gtransform = groupnode.transform
    gclipurl   = groupnode.get('clip-path')
    gmaskurl   = groupnode.get('mask')
    gstyle =  cascaded_style2(groupnode)
            
    els = list(groupnode);
    for el in list(reversed(els)):
        
        unlinkclone = False;
        if isinstance(el,Use):
            useid = el.get('xlink:href');
            if useid is not None:
                useel = getElementById2(get_parent_svg(el),useid[1:]);
                unlinkclone = not(isinstance(useel,(inkex.Symbol)));
        
        if unlinkclone:                                         # unlink clones
            el = unlink2(el);
        elif isinstance(el,lxml.etree._Comment):                # remove comments
            groupnode.remove(el)
            
        if not(isinstance(el, unungroupable)): 
            clippedout = compose_all(el,gclipurl,gmaskurl,gtransform,gstyle)
            if clippedout:
                el.delete()
            else:
                gparent.insert(gindex+1,el); # places above
                
        if isinstance(el, Group) and unlinkclone: # if was a clone, may need to ungroup
            ungroup(el)
    if len(groupnode.getchildren())==0:
        groupnode.delete();

# For composing a group's properties onto its children (also group-like objects like Uses)        
def compose_all(el,clipurl,maskurl,transform,style):
    if style is not None:                                                         # style must go first since we may change it with CSS
        mysty = cascaded_style2(el);
        compsty = style + mysty                
        compsty['opacity']=str(float(mysty.get('opacity','1'))*float(style.get('opacity','1')))  # opacity accumulates at each layer
        el.style = compsty;                                                       
    
    if clipurl is not None:   cout = merge_clipmask(el, clipurl)        # clip applied before transform, fix first
    if maskurl is not None:   merge_clipmask(el, maskurl, mask=True)
    if clipurl is not None:   fix_css_clipmask(el);
    if maskurl is not None:   fix_css_clipmask(el,mask=True);
    
    if transform is not None: el.transform = vmult(transform,el.transform)
    
    if clipurl is None:
        return False
    else:
        return cout

         
# Same as composed_style(), but no recursion and with some tweaks
def shallow_composed_style(el):
    parent = el.getparent();
    if parent.get('opacity') is not None:                          # make sure style includes opacity
        Set_Style_Comp(parent,'opacity',parent.get('opacity'));
    if Get_Style_Comp(parent.style,'stroke-linecap') is not None:  # linecaps not currently inherited, so don't include in composition
        Set_Style_Comp(parent,'stroke-linecap',None);
    if parent is not None and isinstance(parent, ShapeElement):
        return cascaded_style2(parent) + cascaded_style2(el)
    return cascaded_style2(el)


# If an element has clipping/masking specified in a stylesheet, this will override any attributes
# I think this is an Inkscape bug
# Fix by creating a style specific to my id that includes the new clipping/masking
def fix_css_clipmask(el,mask=False):
    if not(mask): cm = 'clip-path'
    else:         cm = 'mask'
    global cssdict
    if cssdict is None:
        generate_cssdict(get_parent_svg(el));
    mycss = cssdict.get(el.get_id());
    if mycss is not None:
        if mycss.get(cm) is not None and mycss.get(cm)!=el.get(cm):
            # get_parent_svg(el).stylesheet.add('#'+el.get_id(),cm+':'+el.get(cm));
            svg = get_parent_svg(el)
            if not(hasattr(svg,'stylesheet_entries')):
                svg.stylesheet_entries = dict();
            svg.stylesheet_entries['#'+el.get_id()]=cm+':'+el.get(cm);
            mycss[cm]=el.get(cm);
    if el.style.get(cm) is not None: # also clear local style
        Set_Style_Comp(el,cm,None);

# Adding to the stylesheet is slow, so as a workaround we only do this once
# There is no good way to do many entries at once, so we do it after we're finished 
def flush_stylesheet_entries(svg):
    if hasattr(svg,'stylesheet_entries'):
        ss = ''
        for k in svg.stylesheet_entries.keys():
            ss += k + '{'+svg.stylesheet_entries[k]+'}\n';
        svg.stylesheet_entries = dict()
        
        stys = svg.xpath('svg:style')
        if len(stys)>0:
            stys[0].text +='\n'+ss+'\n'

# Like duplicate, but randomly sets the id of all descendants also
# Normal duplicate does not
# Second argument disables duplication (for children, whose ids only need to be set)
def duplicate2(el,disabledup=False):
    if not(disabledup):
        # d = el.duplicate();
        d = duplicate_fixed(el);
        dupe_in_cssdict(el.get_id(),d.get_id())
        add_to_iddict(d);
    else:
        d = el;
    for k in d.getchildren():
        oldid = k.get_id();
        set_random_id2(k);
        dupe_in_cssdict(oldid,k.get_id())
        add_to_iddict(k);
        duplicate2(k,True)
    return d
def duplicate_fixed(el): # fixes duplicate's set_random_id
    """Like copy(), but the copy stays in the tree and sets a random id"""
    elem = el.copy()
    el.addnext(elem)
    set_random_id2(elem)
    return elem

# Makes a new object and adds it to the dicts, inheriting CSS dict entry from another element
def new_element(genin,inheritfrom):
    g = genin();                            # e.g Rectangle
    inheritfrom.root.append(g);             # add to the SVG so we can assign an id
    dupe_in_cssdict(get_id2(inheritfrom),get_id2(g))
    add_to_iddict(g);
    return g

# Replace an element with another one
# Puts it in the same location, update the ID dicts
def replace_element(el1,el2):
    # replace el1 with el2
    myp = el1.getparent();
    myi = list(myp).index(el1);
    myp.insert(myi+1,el2);
    
    newid = get_id2(el1);
    oldid = get_id2(el2);
    
    el1.delete();
    el2.set_id(newid)
    add_to_iddict(el2)
    dupe_in_cssdict(oldid,newid)

def intersect_paths(ptha,pthb):
    # Intersect two rectangular paths. Could be generalized later
    ptsa = list(ptha.end_points);
    ptsb = list(pthb.end_points);
    x1c = max(min([p.x for p in ptsa]),min([p.x for p in ptsb]))
    x2c = min(max([p.x for p in ptsa]),max([p.x for p in ptsb]))
    y1c = max(min([p.y for p in ptsa]),min([p.y for p in ptsb]))
    y2c = min(max([p.y for p in ptsa]),max([p.y for p in ptsb]))
    w = x2c-x1c; h=y2c-y1c;
    
    if w>0 and h>0:
        return Path('M '+str(x1c)+','+str(y1c)+' h '+str(w)+' v '+str(h)+' h '+str(-w)+' Z');
    else:
        return Path('')

# Like uniquetol in Matlab
import numpy as np
def uniquetol(A,tol):
    Aa = np.array(A);
    ret = Aa[~(np.triu(np.abs(Aa[:,None] - Aa) <= tol,1)).any(0)]
    return type(A)(ret)

def merge_clipmask(node,newclipurl,mask=False):
# Modified from Deep Ungroup
    def isrectangle(el):
        isrect = False;
        if isinstance(el,(PathElement,Rectangle,Line,Polyline)):
            pth = Path(get_path2(el)).to_absolute();
            pth = pth.transform(el.transform)
            
            pts = list(pth.control_points);
            xs = []; ys = [];
            for p in pts:
                xs.append(p.x); ys.append(p.y)
                
            maxsz = max(max(xs)-min(xs),max(ys)-min(ys))
            tol=1e-3*maxsz;
            if 4<=len(xs)<=5 and len(uniquetol(xs,tol))==2 and len(uniquetol(ys,tol))==2:
                isrect = True;
        if isrect:
            return True,pth
        else:
            return False,None
    def compose_clips(el,ptha,pthb):
        newpath = intersect_paths(ptha,pthb);
        isempty = (str(newpath)=='');
        
        if not(isempty):
            myp = el.getparent();
            p=new_element(PathElement,el); myp.append(p)
            p.set('d',newpath);
        el.delete()
        return isempty # if clipped out, safe to delete element

    if newclipurl is not None:
        svg = get_parent_svg(node);
        cmstr   = 'clip-path'
        if mask: cmstr='mask'
            
        if node.transform is not None:
            # Clip-paths on nodes with a transform have the transform
            # applied to the clipPath as well, which we don't want. 
            # Duplicate the new clip and apply node's inverse transform to its children.
            clippath = getElementById2(svg,newclipurl[5:-1])
            if clippath is not None:    
                d = duplicate2(clippath); 
                svg.defs.append(d)
                if not(hasattr(svg,'newclips')):
                    svg.newclips = []
                svg.newclips.append(d)            # for later cleanup
                for k in list(d):
                    compose_all(k,None,None,-node.transform,None)
                newclipurl = get_id2(d,2)
        
        newclipnode = getElementById2(svg,newclipurl[5:-1]);
        if newclipnode is not None:
            for k in list(newclipnode):
                if isinstance(k,(Use)): k = unlink2(k)

        oldclipurl = node.get(cmstr);
        clipinvalid = True;
        if oldclipurl is not None:
            # Existing clip is replaced by a duplicate, then apply new clip to children of duplicate
            oldclipnode = getElementById2(svg,oldclipurl[5:-1]);
            if oldclipnode is not None:
                clipinvalid = False;
                for k in list(oldclipnode):
                    if isinstance(k,(Use)): k = unlink2(k)
                    
                d = duplicate2(oldclipnode); # very important to use dup2 here
                if not(hasattr(svg,'newclips')):
                    svg.newclips = []
                svg.newclips.append(d)            # for later cleanup
                svg.defs.append(d);               # move to defs
                node.set(cmstr,get_id2(d,2));
                
                newclipisrect = False
                if len(list(newclipnode))==1:
                    newclipisrect,newclippth = isrectangle(list(newclipnode)[0])
                
                couts = [];
                for k in reversed(list(d)): # may be deleting, so reverse
                    oldclipisrect,oldclippth = isrectangle(k)
                    if newclipisrect and oldclipisrect and mask==False:
                        # For rectangular clips, we can compose them easily
                        # Since most clips are rectangles this semi-fixes the PDF clip export bug 
                        cout = compose_clips(k,newclippth,oldclippth); 
                    else:
                        cout = merge_clipmask(k,newclipurl,mask);
                    couts.append(cout)
                cout = all(couts)
        
        if clipinvalid:
            node.set(cmstr,newclipurl)
            cout = False
                
        return cout


# Repeated getElementById lookups can be really slow, so instead create a dict that can be used to 
# speed this up. When an element is created that may be needed later, it MUST be added. 
def getElementById2(svg,elid):
    if not(hasattr(svg,'iddict')):
        generate_iddict(svg);
    iddict = svg.iddict
    return iddict.get(elid);    
def generate_iddict(svg):
    svg.iddict = dict();
    for el in descendants2(svg):
        svg.iddict[get_id2(el)] = el;
def add_to_iddict(el):
    svg = get_parent_svg(el);
    if not(hasattr(svg,'iddict')):
        generate_iddict(svg);
    iddict = svg.iddict
    iddict[get_id2(el)] = el;



# class clipmaskdict():
#     def __init__(self,svg,mask):
#         self.svg   = svg;
#         self.fdict = dict();      # looking up the clip/mask corresponding to an element
#         self.idict = dict();      # looking up the elements corresponding to a clip
        
#         self.mask  = mask;
#         self.cm    =  'clip-path'
#         if mask: self.cm = 'mask'
        
#         for el in descendants2(svg):
#             self.assign_clipmaskdict(el)
    
#     def assign_clipmaskdict(self,el):
#         curl = el.get(self.cm)
#         if curl is not None:
#             cid = curl[5:-1];
#             self.idictappend(cid,el)
#             cel = getElementById2(self.svg, cid);
#             self.fdictappend(el.get_id(),cel)
            
#     def idictappend(self,nid,el): # initialize if no entry, otherwise append
#         cels = self.idict.get(nid);
#         if cels is None:
#             self.idict[nid]=[el]
#         else:
#             self.idict[nid]=list(set(cels+[el]))
#     def fdictappend(self,nid,el):
#         self.fdict[nid]=el
#     def set_new(self,el,newurl):
#         elid=el.get_id();
        
#         oldclip = self.fdict.get(elid)
#         if oldclip is not None:
#             oldid = oldclip.get_id();
#             self.idict[oldid].remove(el); # remove from old clip's inverse dict
        
#         newid = newurl[5:-1];
#         el.set(self.cm,newurl);
#         self.idictappend(newid,el)    # add to new clip's inverse dict
        
#         cel = getElementById2(self.svg, newid);
#         self.fdictappend(elid,cel)
#     def dupe_item(self,orig,dup):
#         myclip = self.fdict.get(orig.get_id());
#         self.fdictappend(dup.get_id(),myclip)
#         if myclip is not None:
#             self.idictappend(myclip.get_id(),dup)
        
# # Generate a dictionary for inverse lookups of clipping/masking
# def generate_clipmaskdict(svg):
#     svg.clipdict = clipmaskdict(svg,False)
#     svg.maskdict = clipmaskdict(svg,True)
# def set_clipmask(el,svg,newurl,mask=False):
#     if not(hasattr(svg,'clipdict')):
#         generate_clipmaskdict(svg)
#     thedict = svg.clipdict;
#     if mask:  thedict = svg.maskdict;
#     thedict.set_new(el,newurl)
# def dupe_in_cmdict(el,dup):
#     svg = get_parent_svg(el)
#     if not(hasattr(svg,'clipdict')):
#         generate_clipmaskdict(svg)
#     d1 = descendants2(el)
#     d2 = descendants2(dup)
#     for ii in range(len(d1)):
#         svg.clipdict.dupe_item(d1[ii],d2[ii])
#         svg.maskdict.dupe_item(d1[ii],d2[ii])

# def prune_clips(svg):
#     if not(hasattr(svg,'clipdict')):
#         generate_clipmaskdict(svg)
#     for d in reversed(descendants2(svg.defs)):
#         did = d.get_id();
#         cps = svg.clipdict.idict.get(did);
#         mks = svg.maskdict.idict.get(did);
#         if cps is not None and mks is not None:
#             if (cps==[] and mks is None) or (mks==[] and cps is None) or (mks==[] and cps==[]):
#                 d.remove()
        
# def delete2(el):
#     svg = get_parent_svg(el)
#     if not(hasattr(svg,'clipdict')):
#         generate_clipmaskdict(svg)
#     elid = el.get_id();
#     if elid in svg.clipdict.fdict.keys():
#         cpid = getElementById2(svg, svg.clipdict.fdict[elid]).get_id();
#         svg.clipdict.idict[cpid].remove(el)
#     if elid in svg.maskdict.fdict.keys():
#         mkid = getElementById2(svg, svg.maskdict.fdict[elid]).get_id();
#         svg.maskdict.idict[cpid].remove(el)
#     el.delete();
    
    
 
# def dupe_in_clipmaskdict(oldid,newid):
#     # duplicate a style in clipmask dicts
#     global cssdict
#     if cssdict is not None:
#         csssty = cssdict.get(oldid);
#         if csssty is not None:
#             cssdict[newid]=csssty;


# The built-in get_unique_id gets stuck if there are too many elements. Instead use an adaptive
# size based on the current number of ids
# Modified from Inkex's get_unique_id
import random
def get_unique_id2(svg, prefix):
    ids = svg.get_ids()
    new_id = None
    size = math.ceil(math.log10(len(ids)))+1
    _from = 10 ** size - 1
    _to = 10 ** size
    while new_id is None or new_id in ids:
        # Do not use randint because py2/3 incompatibility
        new_id = prefix + str(int(random.random() * _from - _to) + _to)
    svg.ids.add(new_id)
    return new_id
# Version that is non-random, useful for debugging
# global idcount
# idcount = 1;
# def get_unique_id2(svg, prefix):
#     ids = svg.get_ids()
#     new_id = None; global idcount
#     while new_id is None or new_id in ids:
#         # Do not use randint because py2/3 incompatibility
#         new_id = prefix + str(idcount); idcount+=1
#     svg.ids.add(new_id)
#     return new_id
def set_random_id2(el, prefix=None, size=4, backlinks=False):
    """Sets the id attribute if it is not already set."""
    prefix = str(el) if prefix is None else prefix
    el.set_id(get_unique_id2(el.root,prefix), backlinks=backlinks)
    
# Like get_id(), but calls set_random_id2
# Modified from Inkex's get_id
def get_id2(el, as_url=0):
    """Get the id for the element, will set a new unique id if not set.
    as_url - If set to 1, returns #{id} as a string
             If set to 2, returns url(#{id}) as a string
    """
    if 'id' not in el.attrib:
        set_random_id2(el,el.TAG)
    eid = el.get('id')
    if as_url > 0:
        eid = '#' + eid
    if as_url > 1:
        eid = f'url({eid})'
    return eid

# e.g., bbs = dh.Get_Bounding_Boxes(self.options.input_file);
def Get_Bounding_Boxes(s=None,getnew=False,filename=None,pxinuu=None,inkscape_binary=None):
# Gets all of a document's bounding boxes (by ID), in user units
# Note that this uses a command line call, so by default it will only get the values from BEFORE the extension is called
# Set getnew to True to make a temporary copy of the file that is then read. 
    if filename is None:
        filename = s.options.input_file;
    if pxinuu is None:
        pxinuu = s.svg.unittouu('1px');
    
    # Query Inkscape
    if not(getnew):
        tFStR = commandqueryall(filename,inkscape_binary=inkscape_binary);
    else:
        tmpname = filename+'_tmp';
        command.write_svg(s.svg,tmpname);
        tFStR = commandqueryall(tmpname,inkscape_binary=inkscape_binary);
        import os; os.remove(tmpname);

    # Parse the output
    tBBLi = tFStR.splitlines()
    bbs=dict();
    for d in tBBLi:
        key = str(d).split(',')[0];
        if key[0:2]=='b\'': # pre version 1.1
            key = key[2:];
        if str(d)[2:52]=='WARNING: Requested update while update in progress':
            continue;                       # skip warnings (version 1.0 only?)
        data = [float(x.strip('\''))*pxinuu for x in str(d).split(',')[1:]]
        bbs[key] = data;
    return bbs

# 2022.02.03: I think the occasional hangs come from the call to command.
# I think this is more robust. Make a tally below if it freezes:
def commandqueryall(fn,inkscape_binary=None):
    if inkscape_binary is None:
        bfn, tmp = Get_Binary_Loc(fn);
    else:
        bfn = inkscape_binary
    arg2 = [bfn, '--query-all',fn]

    p=subprocess_repeat(arg2);
    tFStR = p.stdout
    return tFStR

# In the event of a timeout, repeat subprocess call several times    
def subprocess_repeat(argin):
    BASE_TIMEOUT = 60
    NATTEMPTS = 4
    
    import subprocess
    nfails = 0; ntime = 0;
    for ii in range(NATTEMPTS):
        timeout = BASE_TIMEOUT*(ii+1);
        try:
            p=subprocess.run(argin, shell=False,timeout=timeout,stdout=subprocess.PIPE, stderr=subprocess.DEVNULL);
            break;
        except subprocess.TimeoutExpired:
            nfails+=1; ntime+=timeout;
    if nfails==NATTEMPTS:
        inkex.utils.errormsg('Error: The call to the Inkscape binary timed out '+str(NATTEMPTS)+\
                             ' times in '+str(ntime)+' seconds.\n\n'+\
                             'This may be a temporary issue; try running the extension again.');
        quit()
    else:
        return p
        
global debugs
debugs = ''
def debug(x):
    # inkex.utils.debug(x);
    global debugs
    if debugs!='': debugs += '\n'
    debugs += str(x)
def write_debug():
    global debugs
    if debugs!='':
        debugname = 'Debug.txt'
        f = open(debugname, 'w',encoding="utf-8");
        f.write(debugs);
        f.close();
def idebug(x):
    inkex.utils.debug(x);

def get_parent_svg(el):
    # slightly faster than el.root
    myn = el
    while myn.getparent() is not None:
        myn = myn.getparent();
    if isinstance(myn,SvgDocumentElement):    
        return myn;
    else:
        return None


# Modified from Inkex's get function
# Does not fail on comments
def get_mod(slf, *types):
    def _recurse(elem):
        if (not types or isinstance(elem, types)):
            yield elem
        for child in elem:
            for item in _recurse(child):
                yield item
    return inkex.elements._selected.ElementList(slf.svg, [r for e in slf.values() for r in _recurse(e) \
                                              if not(isinstance(r,lxml.etree._Comment))])




# When non-ascii characters are detected, replace all non-letter characters with the specified font
# Mainly for fonts like Avenir
def Replace_Non_Ascii_Font(el,newfont,*args):
    def nonletter(c):
        return not((ord(c)>=65 and ord(c)<=90) or (ord(c)>=97 and ord(c)<=122))
    def nonascii(c):
        return ord(c)>=128
    def alltext(el):
        astr = el.text;
        if astr is None: astr='';
        for k in el.getchildren():
            if isinstance(k,(Tspan,FlowPara,FlowSpan)):
                astr+=alltext(k)
                tl=k.tail;
                if tl is None: tl=''
                astr+=tl
        return astr
    
    forcereplace = (len(args)>0 and args[0]);
    if forcereplace or any([nonascii(c) for c in alltext(el)]):
        alltxt = [el.text]; el.text=''
        for k in el.getchildren():
            if isinstance(k,(Tspan,FlowPara,FlowSpan)):
                alltxt.append(k)
                alltxt.append(k.tail); k.tail=''
                el.remove(k)
        lstspan = None;
        for t in alltxt:
            if t is None:
                pass
            elif isinstance(t,str):
                ws = []; si=0;
                for ii in range(1,len(t)): # split into words based on whether unicode or not
                    if nonletter(t[ii-1])!=nonletter(t[ii]):
                        ws.append(t[si:ii]);
                        si=ii
                ws.append(t[si:]);
                sty = 'baseline-shift:0%;';
                for w in ws:
                    if any([nonletter(c) for c in w]):
                        w=w.replace(' ','\u00A0'); # spaces can disappear, replace with NBSP
                        ts = Tspan(w,style=sty+'font-family:'+newfont)
                        el.append(ts);
                        lstspan = ts;
                    else:
                        if lstspan is None: el.text = w
                        else:               lstspan.tail = w;
            elif isinstance(t,(Tspan,FlowPara,FlowSpan)):
                Replace_Non_Ascii_Font(t,newfont,True)
                el.append(t);
                lstspan = t;
            
            
                
            
def global_transform(el,trnsfrm,irange=None,trange=None):
    # Transforms an object and fuses it to any paths, preserving stroke
    # If parent layer is transformed, need to rotate out of its coordinate system
    myp = el.getparent();
    if isinstance(myp,SvgDocumentElement):
        prt=Transform([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]);
    else:
        prt=myp.composed_transform(); 
    prt = vmult(Transform('scale('+str(vscale(get_parent_svg(el)))+')'),prt);  # also include document scaling
    
    myt = el.get('transform');
    if myt==None:
        newtr=vmult((-prt),trnsfrm,prt);
        if trange is not None:
            for ii in range(len(trange)):
                trange[ii] = vmult((-prt),trange[ii],prt)
    else:
        newtr=vmult((-prt),trnsfrm,prt,Transform(myt))
        if trange is not None:
            for ii in range(len(trange)):
                trange[ii] = vmult((-prt),trange[ii],prt,Transform(myt))
    
    sw = Get_Composed_Width(el,'stroke-width');
    sd = Get_Composed_List(el, 'stroke-dasharray');
    
    el.set('transform',newtr); # Add the new transform
    ApplyTransform().recursiveFuseTransform(el,irange=irange,trange=trange);
    
    if sw is not None:
        neww, sf, ct, ang = Get_Composed_Width(el,'stroke-width',nargout=4);
        Set_Style_Comp(el,'stroke-width',str(sw/sf));                                            # fix width
    if not(sd in [None,'none']):
        nd,sf = Get_Composed_List(el,'stroke-dasharray',nargout=2);
        Set_Style_Comp(el,'stroke-dasharray',str([sdv/sf for sdv in sd]).strip('[').strip(']')); # fix dash


# Modified from Inkex's get_path          
# Correctly calculates path for rectangles and ellipses  
def get_path2(el):
    class MiniRect(): # mostly from inkex.elements._polygons
        def __init__(self,el):
            self.left = implicitpx(el.get('x', '0'))
            self.top = implicitpx(el.get('y', '0'))
            self.width = implicitpx(el.get('width', '0'))
            self.height = implicitpx(el.get('height', '0'))
            self.rx = implicitpx(el.get('rx', el.get('ry', '0')))
            self.ry = implicitpx(el.get('ry', el.get('rx', '0')))
            self.right = self.left+self.width
            self.bottom = self.top+self.height
        def get_path(self):
            """Calculate the path as the box around the rect"""
            if self.rx:
                rx, ry = self.rx, self.ry # pylint: disable=invalid-name
                return 'M {1},{0.top}'\
                       'L {2},{0.top}    A {0.rx},{0.ry} 0 0 1 {0.right},{3}'\
                       'L {0.right},{4}  A {0.rx},{0.ry} 0 0 1 {2},{0.bottom}'\
                       'L {1},{0.bottom} A {0.rx},{0.ry} 0 0 1 {0.left},{4}'\
                       'L {0.left},{3}   A {0.rx},{0.ry} 0 0 1 {1},{0.top} z'\
                    .format(self, self.left + rx, self.right - rx, self.top + ry, self.bottom - ry)
            return 'M {0.left},{0.top} h{0.width}v{0.height}h{1} z'.format(self, -self.width)
    class MiniEllipse():  # mostly from inkex.elements._polygons
        def __init__(self,el):
            self.cx = implicitpx(el.get('cx', '0'))
            self.cy = implicitpx(el.get('cy', '0'))
            if isinstance(el,(inkex.Ellipse)): # ellipse
                self.rx = implicitpx(el.get('rx', '0'))
                self.ry = implicitpx(el.get('ry', '0'))
            else: # circle
                self.rx = implicitpx(el.get('r', '0'))
                self.ry = implicitpx(el.get('r', '0'))
        def get_path(self):
            return ('M {cx},{y} '
                    'a {rx},{ry} 0 1 0 {rx}, {ry} '
                    'a {rx},{ry} 0 0 0 -{rx}, -{ry} z'
                    ).format(cx=self.cx, y=self.cy-self.ry, rx=self.rx, ry=self.ry)
    if isinstance(el,(inkex.Rectangle)):
        pth = MiniRect(el).get_path()
    elif isinstance(el,(inkex.Circle,inkex.Ellipse)):
        pth = MiniEllipse(el).get_path();
    else:
        pth = el.get_path();
    return pth
otp_support = (inkex.Rectangle,inkex.Ellipse,inkex.Circle,inkex.Polygon,inkex.Polyline,inkex.Line);
def object_to_path(el):
    if not(isinstance(el,(inkex.PathElement,inkex.TextElement))):
        pth = get_path2(el);
        el.tag = '{http://www.w3.org/2000/svg}path';
        el.set('d',str(pth));


# Delete and prune empty ancestor groups       
def deleteup(el):
    myp = el.getparent();
    el.delete()
    if myp is not None:
        myc = myp.getchildren();
        if myc is not None and len(myc)==0:
            deleteup(myp)

# Combines a group of path-like elements
def combine_paths(els,mergeii=0):
    pnew = Path();
    si = [];  # start indices
    for el in els:
        pth = Path(el.get_path()).to_absolute().transform(el.composed_transform());
        if el.get('inkscape-academic-combined-by-color') is None:
            si.append(len(pnew))
        else:
            cbc = el.get('inkscape-academic-combined-by-color') # take existing ones and weld them
            cbc = [int(v) for v in cbc.split()]
            si += [v+len(pnew) for v in cbc[0:-1]]
        for p in pth:
            pnew.append(p)
    si.append(len(pnew))
    
    # Set the path on the mergeiith element
    mel  = els[mergeii]
    if mel.get('d') is None: # Polylines and lines have to be converted to a path
        object_to_path(mel)
    mel.set('d',str(pnew.transform(-mel.composed_transform())));
    
    # Release clips/masks    
    mel.set('clip-path','none'); # release any clips
    mel.set('mask'     ,'none'); # release any masks
    fix_css_clipmask(mel,mask=False) # fix CSS bug
    fix_css_clipmask(mel,mask=True)
    
    mel.set('inkscape-academic-combined-by-color',' '.join([str(v) for v in si]))
    for s in range(len(els)):
        if s!=mergeii:
            deleteup(els[s])    
            
# Gets all of the stroke and fill properties from a style
def get_strokefill(el,styin=None):
    if styin is None:
        sty = selected_style_local(el)
    else:
        sty = styin
    strk = sty.get('stroke',None)
    fill = sty.get('fill',None)
    op     = float(sty.get('opacity',1.0))
    nones = [None,'none','None'];
    if not(strk in nones):    
        strk   = inkex.Color(strk).to_rgb()
        strkl  = strk.lightness
        strkop = float(sty.get('stroke-opacity',1.0))
        strk.alpha = strkop*op
        strkl  = strk.alpha * strkl/255 + (1-strk.alpha)*1; # effective lightness frac with a white bg
        strk.efflightness = strkl
    else:
        strk = None
        strkl = None
    if not(fill in nones):
        fill   = inkex.Color(fill).to_rgb()
        filll  = fill.lightness
        fillop = float(sty.get('fill-opacity',1.0))
        fill.alpha = fillop*op
        filll  = fill.alpha * filll/255 + (1-fill.alpha)*1;  # effective lightness frac with a white bg
        fill.efflightness = filll
    else:
        fill = None
        filll = None
        
    sw = Get_Composed_Width(el, 'stroke-width'   ,styin=sty)
    sd = Get_Composed_List(el, 'stroke-dasharray',styin=sty)
    if sd in nones: sd = None
    if sw in nones or sw==0 or strk is None:
        sw  = None;
        strk= None;
        sd  = None;
        
    ms = sty.get('marker-start',None);
    mm = sty.get('marker-mid',None);
    me = sty.get('marker-end',None);
    
    class StrokeFill():
        def __init__(self,*args):
            (self.stroke,self.fill,self.strokewidth,self.strokedasharray,\
             self.markerstart,self.markermid,self.markerend)=args
    return StrokeFill(strk,fill,sw,sd,ms,mm,me)
        
# Gets the caller's location
import os, sys
def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

# Return a document's visible descendants not in Defs/Metadata/etc
def visible_descendants(svg):
    ndefs = [el for el in list(svg) if not(isinstance(el,((inkex.NamedView, inkex.Defs, \
                                                           inkex.Metadata,  inkex.ForeignObject))))]; 
    return [v for el in ndefs for v in descendants2(el)];

# Gets the location of the Inkscape binary
# Functions copied from command.py
# Copyright (C) 2019 Martin Owens
def Get_Binary_Loc(fin):
    from lxml.etree import ElementTree
    INKSCAPE_EXECUTABLE_NAME = os.environ.get('INKSCAPE_COMMAND')
    if INKSCAPE_EXECUTABLE_NAME == None:
        if sys.platform == 'win32':
            # prefer inkscape.exe over inkscape.com which spawns a command window
            INKSCAPE_EXECUTABLE_NAME = 'inkscape.exe'
        else:
            INKSCAPE_EXECUTABLE_NAME = 'inkscape'
    class CommandNotFound(IOError):
        pass
    class ProgramRunError(ValueError):
        pass
    def which(program):
        if os.path.isabs(program) and os.path.isfile(program):
            return program
        try:
            # Python2 and python3, but must have distutils and may not always
            # work on windows versions (depending on the version)
            from distutils.spawn import find_executable
            prog = find_executable(program)
            if prog:
                return prog
        except ImportError:
            pass
        try:
            # Python3 only version of which
            from shutil import which as warlock
            prog = warlock(program)
            if prog:
                return prog
        except ImportError:
            pass # python2
        raise CommandNotFound(f"Can not find the command: '{program}'")
    def write_svg(svg, *filename):
        filename = os.path.join(*filename)
        if os.path.isfile(filename):
            return filename
        with open(filename, 'wb') as fhl:
            if isinstance(svg, SvgDocumentElement):
                svg = ElementTree(svg)
            if hasattr(svg, 'write'):
                # XML document
                svg.write(fhl)
            elif isinstance(svg, bytes):
                fhl.write(svg)
            else:
                raise ValueError("Not sure what type of SVG data this is.")
        return filename
    def to_arg(arg, oldie=False):
        if isinstance(arg, (tuple, list)):
            (arg, val) = arg
            arg = '-' + arg
            if len(arg) > 2 and not oldie:
                arg = '-' + arg
            if val is True:
                return arg
            if val is False:
                return None
            return f"{arg}={str(val)}"
        return str(arg)
    def to_args(prog, *positionals, **arguments):
        args = [prog]
        oldie = arguments.pop('oldie', False)
        for arg, value in arguments.items():
            arg = arg.replace('_', '-').strip()    
            if isinstance(value, tuple):
                value = list(value)
            elif not isinstance(value, list):
                value = [value]    
            for val in value:
                args.append(to_arg((arg, val), oldie))
        args += [to_arg(pos, oldie) for pos in positionals if pos is not None]
        # Filter out empty non-arguments
        return [arg for arg in args if arg is not None]
    def _call(program, *args, **kwargs):
        stdin = kwargs.pop('stdin', None)
        if isinstance(stdin, str):
            stdin = stdin.encode('utf-8')
        return to_args(which(program), *args, **kwargs)
    def call(program, *args, **kwargs):
        return _call(program, *args, **kwargs)
    def inkscape2(svg_file, *args, **kwargs):
        return call(INKSCAPE_EXECUTABLE_NAME, svg_file, *args, **kwargs)
    return inkscape2(fin)


# Get document location or prompt
def Get_Current_File(ext):
    tooearly = (ivp[0]<=1 and ivp[1]<1);
    if not(tooearly):
        myfile = ext.document_path()
    else:
        myfile = None
        
    if myfile is None or myfile=='':
        if tooearly:
            msg = 'Direct export requires version 1.1.0 of Inkscape or higher.'
        else:
            msg = 'Direct export requires the SVG be saved first. Please save and retry.'
        inkex.utils.errormsg(msg);
        quit()
        return None
    else:
        import os
        return myfile


# Version checking
try:
    inkex_version = inkex.__version__; # introduced in 1.1.2
except:
    try:
        tmp=inkex.BaseElement.unittouu # introduced in 1.1
        inkex_version = '1.1.0'
    except:
        try:
            from inkex.paths import Path, CubicSuperPath
            inkex_version = '1.0.0';
        except:
            inkex_version = '0.92.4';

def vparse(vstr):
    return [int(v) for v in vstr.split('.')]
ivp = vparse(inkex_version);

# Version-specific document scale
def vscale(svg):
    try:
        return svg.oldscale                 # I never change doc size, so it's fine to store it for unnecessary lookups
    except:
        if ivp[0]<=1 and ivp[1]<2:          # pre-1.2: return scale
            svg.oldscale = svg.scale
        else:                               # post-1.2: return old scale
            scale_x = float(svg.unittouu(svg.get('width')))/ float(svg.get_viewbox()[2])
            scale_y = float(svg.unittouu(svg.get('height'))) / float(svg.get_viewbox()[3])
            svg.oldscale = max([scale_x, scale_y])
            return svg.oldscale
        return svg.oldscale
    
# Version-specific multiplication
def vmult(*args):
    outval = args[-1];
    for ii in reversed(range(0,len(args)-1)):
        if ivp[0]<=1 and ivp[1]<2:      # pre-1.2: use asterisk
            outval = args[ii]*outval;
        else:                           # post-1.2: use @
            outval = args[ii]@outval;
    return outval

def isMask(el):
    if ivp[0]<=1 and ivp[1]<2:          # pre-1.2: check tag
        return (el.tag[-4:]=='mask')
    else:               
        return isinstance(el, (inkex.Mask))
    
def vto_xpath(sty):
    if ivp[0]<=1 and ivp[1]<2:      # pre-1.2: use v1.1 version of to_xpath from inkex.Style
        import re
        step_to_xpath = [
            (re.compile(r'\[(\w+)\^=([^\]]+)\]'), r'[starts-with(@\1,\2)]'), # Starts With
            (re.compile(r'\[(\w+)\$=([^\]]+)\]'), r'[ends-with(@\1,\2)]'), # Ends With
            (re.compile(r'\[(\w+)\*=([^\]]+)\]'), r'[contains(@\1,\2)]'), # Contains
            (re.compile(r'\[([^@\(\)\]]+)\]'), r'[@\1]'), # Attribute (start)
            (re.compile(r'#(\w+)'), r"[@id='\1']"), # Id Match
            (re.compile(r'\s*>\s*([^\s>~\+]+)'), r'/\1'), # Direct child match
            #(re.compile(r'\s*~\s*([^\s>~\+]+)'), r'/following-sibling::\1'),
            #(re.compile(r'\s*\+\s*([^\s>~\+]+)'), r'/following-sibling::\1[1]'),
            (re.compile(r'\s*([^\s>~\+]+)'), r'//\1'), # Decendant match
            (re.compile(r'\.([-\w]+)'), r"[contains(concat(' ', normalize-space(@class), ' '), ' \1 ')]"),
            (re.compile(r'//\['), r'//*['), # Attribute only match
            (re.compile(r'//(\w+)'), r'//svg:\1'), # SVG namespace addition
        ]
        def style_to_xpath(styin):
            return '|'.join([rule_to_xpath(rule) for rule in styin.rules])
        def rule_to_xpath(rulein):
            ret = rulein.rule
            for matcher, replacer in step_to_xpath:
                ret = matcher.sub(replacer, ret)
            return ret
        return style_to_xpath(sty)
    else:
        return sty.to_xpath();
    
def Version_Check(caller):
    siv = 'v1.4.13'         # Scientific Inkscape version
    maxsupport = '1.2.0';
    minsupport = '1.1.0';
    
    logname = 'Log.txt'
    NFORM = 200;
    
    maxsupp = vparse(maxsupport);
    minsupp = vparse(minsupport);
    
    try:
        f = open(logname,'r');
        d = f.readlines(); f.close();
    except:
        d = [];    
    
    displayedform = False;
    if len(d)>0:
        displayedform = d[-1]=='Displayed form screen'
        if displayedform:
            d=d[:len(d)-1];
    
    prevvp = [vparse(dv[-6:]) for dv in d]
    if (ivp[0]<minsupp[0] or ivp[1]<minsupp[1]) and not(ivp in prevvp):
        msg = 'Scientific Inkscape requires Inkscape version '+minsupport+' or higher. '+\
              'You are running a less-recent version—it might work, it might not.\n\nThis is a one-time message.\n\n';
        inkex.utils.errormsg(msg);
    if (ivp[0]>maxsupp[0] or ivp[1]>maxsupp[1]) and not(ivp in prevvp):
        msg = 'Scientific Inkscape requires Inkscape version '+maxsupport+' or lower. '+\
              'You are running a more-recent version—you must be from the future!\n\n'+\
              'It might work, it might not. Check if there is a more recent version of Scientific Inkscape available. \n\nThis is a one-time message.\n\n';
        inkex.utils.errormsg(msg);
    
    from datetime import datetime
    dt = datetime.now().strftime("%Y.%m.%d, %H:%M:%S")
    d.append(dt+' Running '+caller+' '+siv+', Inkscape v'+inkex_version+'\n');
    
    if len(d)>NFORM:
        d = d[-NFORM:];
        if not(displayedform):
            sif3 = 'dt9mt3Br6';
            sif1 = 'https://forms.gle/'
            sif2 = 'RS6HythP';
            msg = 'You have run Scientific Inkscape extensions over '+\
                str(NFORM)+' times! Thank you for being such a dedicated user!'+\
                '\n\nBuilding and maintaining Scientific Inkscape is a time-consuming job,'+\
                ' and I have no real way of tracking the number of active users. For reporting purposes, I would greatly '+\
                "appreciate it if you could sign my guestbook to indicate that you use Scientific Inkscape. "+\
                'It is located at\n\n'+sif1+sif2+sif3+'\n\nPlease note that this is a one-time message. '+\
                'You will never get this message again, so please copy the URL before you click OK.\n\n';
            inkex.utils.errormsg(msg);
        d.append('Displayed form screen')

    try:        
        f = open(logname, 'w');
        f.write(''.join(d));
        f.close();
    except:
        inkex.utils.errormsg('Error: You do not have write access to the directory where the Scientific Inkscape '+\
                             'extensions are installed. You may have not installed them in the correct location. '+\
                             '\n\nMake sure you install them in the User Extensions directory, not the Inkscape Extensions '+\
                             'directory.');
        quit();
    
