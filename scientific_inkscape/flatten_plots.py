#!/usr/bin/env python 
# coding=utf-8
#
# Copyright (C) 2021 David Burghoff, dburghoff@nd.edu
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
#



import inkex
from inkex import (TextElement, FlowRoot, FlowPara, FlowRegion, Tspan, TextPath, Rectangle,\
                   PathElement, Line, Path,StyleElement,\
                   NamedView, Defs, Metadata, ForeignObject,Group)

import os,sys
sys.path.append(os.path.dirname(os.path.realpath(sys.argv[0]))) # make sure my directory is on the path
import dhelpers as dh

import lxml, os
import RemoveKerning, Style2


class FlattenPlots(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--tab", help="The selected UI-tab when OK was pressed")
        pars.add_argument("--deepungroup", type=inkex.Boolean, default=True,help="Deep ungroup")
        pars.add_argument("--fixtext", type=inkex.Boolean, default=True, help="Text fixes")
        pars.add_argument("--removerectw", type=inkex.Boolean, default=True, help="Remove white rectangles")
        pars.add_argument("--splitdistant", type=inkex.Boolean, default=True, help="Split distant text")
        pars.add_argument("--mergenearby", type=inkex.Boolean, default=True, help="Merge nearby text")
        pars.add_argument("--fixshattering", type=inkex.Boolean, default=True, help="Fix text shattering")
        pars.add_argument("--mergesubsuper", type=inkex.Boolean, default=True, help="Import superscripts and subscripts")
        pars.add_argument("--setreplacement", type=inkex.Boolean, default=False, help="Replace missing fonts")
        pars.add_argument("--replacement", type=str, default='Arial', help="Missing font replacement");
        pars.add_argument("--justification", type=int, default=1, help="Text justification");
        pars.add_argument("--testmode", type=inkex.Boolean, default=False, help="Test mode");

    def runflatten(self):
        poprest = self.options.deepungroup
        removerectw = self.options.removerectw
        splitdistant = self.options.splitdistant and self.options.fixtext
        fixshattering = self.options.fixshattering and self.options.fixtext
        mergesubsuper = self.options.mergesubsuper and self.options.fixtext
        mergenearby = self.options.mergenearby and self.options.fixtext
        setreplacement = self.options.setreplacement and self.options.fixtext
        replacement = self.options.replacement
        
        sel = [self.svg.selection[ii] for ii in range(len(self.svg.selection))]; # should work with both v1.0 and v1.1
        
        # For testing, duplicate selection and flatten its elements
        # self.svg.selection = [self.svg.getElementById('layer1')]
        # self.options.testmode = True
        if self.options.testmode: # 
            import random
            random.seed(1)
            sel = [self.svg.selection[ii] for ii in range(len(self.svg.selection))]; # should work with both v1.0 and v1.1
            for el in sel:
                d=dh.duplicate2(el);
                el.getparent().insert(list(el.getparent()).index(el),d)
                if d.get('inkscape:label') is not None:
                    el.set('inkscape:label',el.get('inkscape:label')+' flat')
                    d.set('inkscape:label',d.get('inkscape:label')+' original')
                d.set('sodipodi:insensitive','true'); # lock original
                d.set('opacity',0.3);
            sel = [list(el) for el in sel]
            import itertools
            sel = list(itertools.chain.from_iterable(sel))
            
        
        seld = [v for el in sel for v in dh.descendants2(el)];
        
        # Move selected defs/clips/mask into global defs
        if poprest:
            seldefs = [el for el in seld if isinstance(el,Defs)];
            for el in seldefs:
                self.svg.defs.append(el)
                for d in dh.descendants2(el):
                    if d in seld: seld.remove(d) # no longer selected
            selcm = [el for el in seld if isinstance(el, (inkex.ClipPath)) or dh.isMask(el)];
            for el in selcm:
                self.svg.defs.append(el)
                for d in dh.descendants2(el):
                    if d in seld: seld.remove(d) # no longer selected
        
        
        gs = [el for el in seld if isinstance(el,Group)]
        obs = [el for el in seld if not(isinstance(el, (NamedView, Defs, Metadata, ForeignObject,Group)))]
        
        if len(gs)==0 and len(obs)==0:
            inkex.utils.errormsg('No objects selected!'); return;
        
        if poprest:
            for g in list(reversed(gs)):
                ks = g.getchildren()
                if any([isinstance(k,lxml.etree._Comment) for k in ks]) and \
                   all([isinstance(k,(lxml.etree._Comment,Defs)) or k.get('unlinked_clone')=='True' for k in ks]):
                    # Leave Matplotlib text glyphs grouped together 
                    cmnt = ';'.join([str(k).strip('<!-- ').strip(' -->') for k in ks if isinstance(k,lxml.etree._Comment)]);
                    g.set('mpl_comment',cmnt)
                    [g.remove(k) for k in ks if isinstance(k,lxml.etree._Comment)]; # remove comment, but leave grouped
                elif g.get('mpl_comment') is not None: pass
                else:
                    dh.ungroup(g);
            dh.flush_stylesheet_entries(self.svg)
            
        
        if self.options.fixtext:
            if setreplacement:
                for el in obs:
                    if isinstance(el,(TextElement,Tspan)) and el.getparent() is not None: # textelements not deleted
                        ff = dh.selected_style_local(el).get('font-family');
                        dh.Set_Style_Comp(el,'-inkscape-font-specification',None)
                        if ff==None or ff=='none' or ff=='':
                            dh.Set_Style_Comp(el,'font-family',replacement)
                        elif ff==replacement:
                            pass
                        else:
                            ff = [x.strip('\'').strip() for x in ff.split(',')]
                            if not(ff[-1].lower()==replacement.lower()):
                                ff.append(replacement)
                            dh.Set_Style_Comp(el,'font-family',','.join(ff))   
                            
            if fixshattering or mergesubsuper or splitdistant or mergenearby:
                if self.options.justification==1:
                    justification = 'middle';
                elif self.options.justification==2:
                    justification = 'start';
                elif self.options.justification==3:
                    justification = 'end';
                elif self.options.justification==4:
                    justification = None;
                obs = RemoveKerning.remove_kerning(self,obs,fixshattering,mergesubsuper,splitdistant,mergenearby,justification) 

        
        if removerectw:
            for el in obs:
                if isinstance(el, (PathElement, Rectangle, Line)):
                    pts=list(Path(dh.get_path2(el)).end_points);
                    xs = [p.x for p in pts]; ys = [p.y for p in pts]
                    
                    if len(xs)>0:
                        maxsz = max(max(xs)-min(xs),max(ys)-min(ys))
                        tol=1e-3*maxsz;
                        if isinstance(el, (Rectangle)) or \
                            4<=len(xs)<=5 and len(dh.uniquetol(xs,tol))==2 and len(dh.uniquetol(ys,tol))==2: # is a rectangle
                            sf  = dh.get_strokefill(el)
                            if sf.stroke is None and sf.fill is not None and tuple(sf.fill)==(255,255,255,1):
                                dh.deleteup(el)
                        
                        # sty=dh.selected_style_local(el);
                        # fill = sty.get('fill');
                        # strk = sty.get('stroke');
                        # opacity = sty.get('opacity')
                        # if opacity is None: opacity = 1;
                        # if (fill in ['#ffffff','white'] and \
                        #     strk in [None,'none'] and \
                        #     opacity==1):
                        #     el.delete()
    
    
        # Remove any unused clips we made, unnecessary white space in document
        # import time
        # tic = time.time();
        # ds = dh.descendants2(self.svg);
        ds = self.svg.ldescendants;                
        clips = [el.get('clip-path') for el in ds]; 
        masks = [el.get('mask')      for el in ds]; 
        clips = [url[5:-1] for url in clips if url is not None];
        masks = [url[5:-1] for url in masks if url is not None];
        if hasattr(self.svg,'newclips'):
            for el in self.svg.newclips:
                if isinstance(el,(inkex.ClipPath)) and not(dh.get_id2(el) in clips):
                    dh.deleteup(el)
                elif dh.isMask(el) and not(dh.get_id2(el) in masks):
                    dh.deleteup(el)

        for el in reversed(ds):
            if not(isinstance(el,(Tspan, FlowPara, FlowRegion, TextPath))):
                if el.tail is not None: el.tail = None
            if not(isinstance(el,(StyleElement,TextElement,Tspan,\
                                  FlowRoot,FlowPara,FlowRegion,TextPath))):
                if el.text is not None: el.text = None

        # dh.debug(time.time()-tic)


    def effect(self): 
        cprofile = True;
        cprofile = False;
        lprofile = True;
        lprofile = False;
        
        if cprofile or lprofile:
            import io
            if self.options.testmode:
                # print(self.options.output)
                profiledir = os.path.split(os.path.abspath(str(self.options.output)))[0];
                cprofile = True;
            else:
                profiledir = dh.get_script_path();
        
        if cprofile:
            import cProfile, pstats
            from pstats import SortKey
            pr = cProfile.Profile()
            pr.enable()
        
        needtorun = True;
        if lprofile:
            try:
                from line_profiler import LineProfiler
                lp = LineProfiler()
                
                
                import TextParser
                from inspect import getmembers, isfunction, isclass,getmodule
                fns = []
                for m in [dh,TextParser,RemoveKerning,Style2]:
                    fns += [v[1] for v in getmembers(m,isfunction)]
                    for c in getmembers(m,isclass):
                        if getmodule(c[1]) is m:
                            fns += [v[1] for v in getmembers(c[1],isfunction)]
                            for p in getmembers(c[1],lambda o: isinstance(o, property)):
                                if p[1].fget is not None:
                                    fns += [p[1].fget]
                                if p[1].fset is not None:
                                    fns += [p[1].fset]
                for fn in fns:
                    lp.add_function(fn)
                lpw = lp(self.runflatten)
                lpw()
                stdouttrap = io.StringIO()
                lp.print_stats(stdouttrap);
                
                ppath = os.path.abspath(os.path.join(profiledir,'lprofile.csv'))
                result=stdouttrap.getvalue()
                f=open(ppath,'w',encoding="utf-8");
                f.write(result); f.close();
                needtorun = False;
            except: pass
        
        if needtorun:
            self.runflatten()
        
        if cprofile:
            pr.disable()
            s = io.StringIO()
            sortby = SortKey.CUMULATIVE
            pr.dump_stats(os.path.abspath(os.path.join(profiledir,'cprofile.prof')))
            ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
            ps.print_stats()
            ppath = os.path.abspath(os.path.join(profiledir,'cprofile.csv'))
            
            result=s.getvalue()
            prefix = result.split('ncalls')[0];
            # chop the string into a csv-like buffer
            result='ncalls'+result.split('ncalls')[-1]
            result='\n'.join([','.join(line.rstrip().split(None,5)) for line in result.split('\n')])
            result=prefix+'\n'+result;
            f=open(ppath,'w');
            f.write(result); f.close();
                            

if __name__ == '__main__':
    dh.Version_Check('Flattener')
    try:
        s=FlattenPlots().run()
        dh.write_debug();
    except lxml.etree.XMLSyntaxError:
        inkex.utils.errormsg('Error parsing XML! Extensions can only run on SVG files. If this is a file imported from another format, try saving as an SVG or pasting the contents into a new SVG.');
