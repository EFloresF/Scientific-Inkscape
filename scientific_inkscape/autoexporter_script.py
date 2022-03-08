# Inkscape Auto-Exporter, by David Burghoff
# Service that checks a folder for changes in svg files, and then exports them 
# automatically to another folder in multiple formats.

BASE_TIMEOUT = 60; 
MAX_ATTEMPTS = 4;
DEBUG = False;


import sys, platform, subprocess, os, threading, datetime, time,copy,pickle
import numpy as np
mypath = os.path.dirname(os.path.realpath(sys.argv[0]));
f=open(os.path.join(mypath,'ae_settings.p'),'rb');
s=pickle.load(f); f.close(); os.remove(os.path.join(mypath,'ae_settings.p'));

watchdir = s[0]; writedir = s[1]; bfn = s[2]; fmts= s[3]; 
sys.path += s[4];
PNG_DPI = s[5]
imagedpi = s[6]
reduce_images = s[7]
tojpg = s[8]
text_to_paths = s[9]
thinline_dehancement = s[10]

import inkex
from inkex import Vector2d, Transform
import dhelpers as dh

try:
    import tkinter
    from tkinter import filedialog
    promptstring = '\nEnter D to change directories, R to change DPI, F to export a file, A to export all now, and Q to quit: '
    hastkinter = True
except:
    promptstring = '\nEnter A to export all now, R to change DPI, and Q to quit: '
    hastkinter = False

fmts = [(v.lower()=='true') for v in fmts.split('_')];
exp_fmts = []
if fmts[0]: exp_fmts.append('pdf')
if fmts[1]: exp_fmts.append('png')
if fmts[2]: exp_fmts.append('emf')
if fmts[3]: exp_fmts.append('eps')
if fmts[4]: exp_fmts.append('svg')


if platform.system().lower()=='darwin': print(' ')
print('Scientific Inkscape Autoexporter')
print('\nPython interpreter: '+sys.executable)
print('Inkscape binary: '+bfn+'')

import image_helpers as ih
if not(ih.hasPIL):
    print('Python does not have PIL, images will not be cropped or converted to JPG\n')
else:
    print('Python has PIL\n')


# Use the Inkscape binary to export the file
def export_file(bfn,fin,fout,fformat,ppoutput=None):
    import os; 
    myoutput = fout[0:-4] + '.' + fformat
    print('    To '+fformat+'...',end=' ',flush=True)
    timestart = time.time();
    
    if ppoutput is not None:
        fin, tmpoutputs, tempdir = ppoutput
    else:
        tmpoutputs = []; tempdir = None
    
    try:
        smallsvg = (fformat=='svg')
        notpng = not(fformat=='png')
        if (thinline_dehancement or smallsvg) and notpng:
            if tempdir is None:
                import tempfile
                tempdir = os.path.realpath(tempfile.mkdtemp(prefix="ae-"));
                if DEBUG:
                    print('\n    '+joinmod(tempdir,''))
            basetemp = joinmod(tempdir,'tmp.svg');
#            print(basetemp)
        
        
        if thinline_dehancement and notpng:
            svg = load_svg_clear_dict(fin);
            Thinline_Dehancement(svg,fformat)
            tmp1 = basetemp.replace('.svg','_tld'+fformat[0]+'.svg');
            overwrite_svg(svg,tmp1);
            fin = copy.copy(tmp1);  tmpoutputs.append(tmp1)
        
        if smallsvg: # Convert to pdf, then to a smaller SVG
            tmp3 = basetemp.replace('.svg','_tmp_small.pdf')
            arg2 = [bfn, '--export-background','#ffffff','--export-background-opacity','1.0','--export-dpi',\
                                    str(PNG_DPI),'--export-filename',tmp3,fin]
            dh.subprocess_repeat(arg2);
            fin = copy.copy(tmp3);  tmpoutputs.append(tmp3)
            myoutput = myoutput.replace('.svg','_smaller.svg')
            
        try: os.remove(myoutput);
        except: pass
        arg2 = [bfn, '--export-background','#ffffff','--export-background-opacity','1.0','--export-dpi',\
                                str(PNG_DPI),'--export-filename',myoutput,fin]
        dh.subprocess_repeat(arg2);
            
        print('done! (' + str(round(1000*(time.time()-timestart))/1000) + ' s)');
        return True, tmpoutputs, myoutput
    except:
        print('Error writing to file')
        return False, tmpoutputs, None

def preprocessing(bfn,fin,fout):
    import os; 
    print('    Preprocessing...',end=' ',flush=True); timestart = time.time();
    try:
        tmpoutputs = [];
        import tempfile
        tempdir = os.path.realpath(tempfile.mkdtemp(prefix="ae-"));
        if DEBUG:
            print('\n    '+joinmod(tempdir,''))
        basetemp = joinmod(tempdir,'tmp.svg');
        
        if reduce_images:
            import image_helpers as ih
            # print(ih.hasPIL)
            svg = load_svg_clear_dict(fin);
            els = [el for el in dh.visible_descendants(svg) if isinstance(el,(inkex.Image))]
            if len(els)>0:     
                bbs = dh.Get_Bounding_Boxes(filename=fin,pxinuu=svg.unittouu('1px'),inkscape_binary=bfn)
                imgtype = 'png';
                acts = ''; acts2=''
                tis = []; ti2s = [];
                for el in els:
                    tmpimg = basetemp.replace('.svg','_im_'  +el.get_id()+'.'+imgtype);  tis.append(tmpimg )
                    tmpimg2= basetemp.replace('.svg','_imbg_'+el.get_id()+'.'+imgtype); ti2s.append(tmpimg2)
                    acts+= 'export-id:'+el.get_id()+'; export-id-only; export-dpi:'+str(imagedpi)+\
                           '; export-filename:'+tmpimg+'; export-do; '  # export item only
                    acts2+='export-id:'+el.get_id()+'; export-dpi:'+str(imagedpi)+\
                           '; export-filename:'+tmpimg2+'; export-background-opacity:1.0; export-do; ' # export all w/background
                arg2 = [bfn, '--actions',acts,fin]
                dh.subprocess_repeat(arg2);
                if tojpg and ih.hasPIL:
                    arg2 = [bfn, '--actions',acts2,fin]
                    dh.subprocess_repeat(arg2);
                
                for ii in range(len(els)):
                    el = els[ii]; tmpimg = tis[ii]; tmpimg2= ti2s[ii];
                    if os.path.exists(tmpimg):
                        tmpoutputs.append(tmpimg);
                        if ih.hasPIL:
                            if tojpg:
                                tmpoutputs.append(tmpimg2)
                                tmpjpg = tmpimg.replace('.png','.jpg')
                                ret, bbox = ih.to_jpeg(tmpimg,tmpimg2,tmpjpg);
                                
                                tmpoutputs.append(tmpjpg)
                                tmpimg = copy.copy(tmpjpg);
                            else:
                                tmpimg, bbox = ih.crop_image(tmpimg);
                        ih.embed_external_image(el,tmpimg); 
                        
                        # The exported image has a different size and shape than the original
                        # Correct by putting transform/clip/mask on a new parent group, then fix location, then ungroup
                        g = inkex.Group()
                        myi = list(el.getparent()).index(el)
                        el.getparent().insert(myi+1,g); # place group above
                        g.insert(0,el);                 # move image to group
                        g.set('transform',el.get('transform')); el.set('transform',None)
                        g.set('clip-path',el.get('clip-path')); el.set('clip-path',None)
                        g.set('mask'     ,el.get('mask')     ); el.set('mask'     ,None)
                        
                        
                        # Calculate what transform is needed to preserve the image's location
                        ct = dh.vmult(Transform('scale('+str(dh.vscale(svg))+')'),el.composed_transform());
                        bb = bbs[el.get_id()];
    #                    print(bb)
                        pbb = [Vector2d(bb[0],bb[1]),Vector2d(bb[0]+bb[2],bb[1]),\
                               Vector2d(bb[0]+bb[2],bb[1]+bb[3]),Vector2d(bb[0],bb[1]+bb[3])]; # top-left,tr,br,bl
                        put = [(-ct).apply_to_point(p) for p in pbb]   # untransformed bbox (where the image needs to go)
                        
                        
                        myx = dh.implicitpx(el.get('x'));     myy = dh.implicitpx(el.get('y'));
                        if myx is None: myx = 0;
                        if myy is None: myy = 0;
                        myw = dh.implicitpx(el.get('width')); myh = dh.implicitpx(el.get('height'));
                        pgo = [Vector2d(myx,myy),        Vector2d(myx+myw,myy),\
                               Vector2d(myx+myw,myy+myh),Vector2d(myx,myy+myh)]; # where the image is
                        el.set('preserveAspectRatio','none')  # prevents aspect ratio snapping
                        
                        a = np.array([[pgo[0].x,0,pgo[0].y,0,1,0],
                                      [0,pgo[0].x,0,pgo[0].y,0,1],
                                      [pgo[1].x,0,pgo[1].y,0,1,0],
                                      [0,pgo[1].x,0,pgo[1].y,0,1],
                                      [pgo[2].x,0,pgo[2].y,0,1,0],
                                      [0,pgo[2].x,0,pgo[2].y,0,1]]);
                        b = np.array([[put[0].x,put[0].y,put[1].x,put[1].y,put[2].x,put[2].y]]).T
                        T = np.linalg.solve(a,b);
                        T = 'matrix('+','.join([str(v[0]) for v in T])+')';
                        el.set('transform',T)
                        
                        # If we cropped, need to modify location according to bbox
                        if ih.hasPIL and bbox is not None:
                            el.set('x',str(myx + bbox[0]*myw));
                            el.set('y',str(myy + bbox[1]*myh));
                            el.set('width',str((bbox[2]-bbox[0])*myw));
                            el.set('height',str((bbox[3]-bbox[1])*myh));
                        dh.ungroup(g)
                
                tmp4 = basetemp.replace('.svg','_eimg.svg');
                overwrite_svg(svg,tmp4);
                fin = copy.copy(tmp4);  tmpoutputs.append(tmp4)

        # if (text_to_paths or thinline_dehancement) and notpng:
        if text_to_paths:
            svg = load_svg_clear_dict(fin);
            ds = dh.visible_descendants(svg)
            
            tels = [el.get_id() for el in ds if isinstance(el,(inkex.TextElement))]                       # text-like
            # pels = [el.get_id() for el in ds if isinstance(el,dh.otp_support) or el.get('d') is not None] # path-like
            # stroke to path too buggy for now, don't convert strokes
            convert_els=[];
            if text_to_paths:         convert_els+=tels
            # if thinline_dehancement:  convert_els+=pels
            
            celsj = ','.join(convert_els);
            tmp2= basetemp.replace('.svg','_stp.svg');
            arg2 = [bfn, '--actions','select:'+celsj+'; object-stroke-to-path; export-filename:'+tmp2+'; export-do',fin]
            dh.subprocess_repeat(arg2);
            
            if text_to_paths:
                # Text converted to paths are a group of characters. Combine them all
                svg = load_svg_clear_dict(tmp2);
                for elid in tels:
                    el = dh.getElementById2(svg, elid)
                    if el is not None and len(list(el))>0:
                        dh.combine_paths(list(el))
                        # dh.ungroup(el)
                overwrite_svg(svg,tmp2);
            fin = copy.copy(tmp2);  tmpoutputs.append(tmp2)       
        print('done! (' + str(round(1000*(time.time()-timestart))/1000) + ' s)');
        return (fin, tmpoutputs, tempdir)
    except:
        pass        

def Get_Directories():
    root = tkinter.Tk(); root.geometry("1x1"); root.lift(); root.overrideredirect(1); 
    print('Select a directory to watch');
    watchdir = tkinter.filedialog.askdirectory(title='Select a directory to watch'); root.destroy();    
    if watchdir=='': raise  
    root = tkinter.Tk(); root.geometry("1x1"); root.lift(); root.overrideredirect(1); 
    print('Select a directory to write to');
    writedir = tkinter.filedialog.askdirectory(title='Select a directory to write to'); root.destroy();
    if writedir=='': raise  
    return watchdir,writedir


def Get_File(initdir):
    root = tkinter.Tk(); root.geometry("1x1"); root.lift(); root.overrideredirect(1); 
    print('Select a file to export');
    selectedfile = tkinter.filedialog.askopenfile(title='Select a file'); root.destroy();
    selectedfile.close()   
    return selectedfile.name
        
# Convenience functions
def joinmod(dirc,f):
    return os.path.join(os.path.abspath(dirc),f)
def timenow():
    return datetime.datetime.now().timestamp();
def overwrite_svg(svg,fn):
    try: os.remove(fn)
    except: pass
    inkex.command.write_svg(svg,fn);
    
from inkex import load_svg
def load_svg_clear_dict(fin):
    svg = load_svg(fin).getroot();
    # print(svg.iddict)  
    # dh.iddict = None # only valid one svg at a time
    return svg
def get_defs(svg):
    for k in list(svg):
        if isinstance(k,(inkex.Defs)):
            return k
    d = inkex.Defs();  # no Defs, make one
    svg.insert(len(list(svg)),d)
    return d


# Get svg files in all subdirectories
def get_files(dirin,direxclude):
    fs = []
    # for d in os.walk(dirin):
    #     if direxclude is None or not(os.path.abspath(d[0])==os.path.abspath(direxclude)):
    #         for f in d[2]:
    #             if f[-4:]=='.svg':
    #                 fs.append(os.path.join(os.path.abspath(d[0]),f))
    for f in os.scandir(dirin):
        if f.name[-4:]=='.svg':
            fs.append(os.path.join(os.path.abspath(dirin),f.name))
    return fs

def Thinline_Dehancement(svg,fformat):
# Prevents thin-line enhancement in certain bad PDF renderers (*cough* Adobe Acrobat *cough*)
# For PDFs, turn any straight lines into a Bezier curve
# For EMFs, add an extra node to straight lines (only works for fills, not strokes currently)
# Doing both doesn't work: extra nodes removes the Bezier on conversion to PDF, Beziers removed on EMF
    pth_commands = ['M', 'm', 'L', 'l', 'H', 'h', 'V', 'v', 'C', 'c', 'S', 's', 'Q', 'q', 'T', 't', 'A', 'a', 'Z', 'z'];
    for el in dh.descendants2(svg):
        if isinstance(el,dh.otp_support):
            dh.object_to_path(el);
        d = el.get('d');
        if d is not None and any([cv in d for cv in ['h','v','l','H','V','L']]):
            if any([cv in d for cv in ['H','V','L']]):
                d = str(inkex.Path(d).to_relative());
            ds = d.replace(',',' ').split(' ')
            nexth = False; nextv = False; nextl = False;
            ii=0;
            while ii<len(ds):
                if ds[ii]=='v':
                    nextv = True; nexth = False; nextl = False;
                    ds[ii] = ''
                elif ds[ii]=='h':
                    nexth = True; nextv = False; nextl = False;
                    ds[ii] = ''
                elif ds[ii]=='l':
                    nextl = True; nextv = False; nexth = False;
                    ds[ii] = '';
                elif ds[ii] in pth_commands:
                    nextv = False; nexth = False; nextl = False;
                else:
                    if nexth:
                        if fformat=='emf':
                            hval = float(ds[ii]);
                            ds[ii] = 'h '+str(hval/2)+' '+str(hval/2)
                            # ds[ii] = 'c '+str(hval/2)+',0 '+str(hval/2)+',0 '+str(hval/2)+',0'
                            # ds[ii] = ds[ii]+' '+ds[ii]
                        else:
                            ds[ii] = 'c '+ds[ii]+',0 '+ds[ii]+',0 '+ds[ii]+',0'
                    elif nextv:
                        if fformat=='emf':
                            vval = float(ds[ii]);
                            ds[ii] = 'v '+str(vval/2)+' '+str(vval/2)
                            # ds[ii] = 'c 0,'+str(vval/2)+' 0,'+str(vval/2)+' 0,'+str(vval/2)
                            # ds[ii] = ds[ii]+' '+ds[ii]
                        else:
                            ds[ii] = 'c 0,'+ds[ii]+' 0,'+ds[ii]+' 0,'+ds[ii]
                    elif nextl:
                        if fformat=='emf':
                            lx = float(ds[ii]);
                            ly = float(ds[ii+1]);
                            ds[ii] = 'l '+str(lx/2)+','+str(ly/2)+' '+str(lx/2)+','+str(ly/2)
                            # ds[ii] = 'c '+str(lx/2)+','+str(ly/2)+' '+str(lx/2)+','+str(ly/2)+' '+str(lx/2)+','+str(ly/2);
                            # ds[ii] = ds[ii]+' '+ds[ii]
                        else:
                            ds[ii] = 'c '+ds[ii]+','+ds[ii+1]+' '+ds[ii]+','+ds[ii+1]+' '+ds[ii]+','+ds[ii+1];
                        ds[ii+1] = ''; ii+=1
                ii+=1
            newd = ' '.join(ds);
            newd = newd.replace('  ',' ')
            el.set('d',newd)


# Threading class
class myThread(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.stopped = False
        self.ui = None  # user input
        self.nf = True;  # new folder
        self.ea = False; # export all
        self.es = False; # export selected
        self.dm = False; # debug mode
    def run(self):
        if self.threadID==1:
        # Main thread
            ltm = timenow();
            genfiles = [];
            while not(self.stopped):
                if self.nf:
                    print('Export formats: '+', '.join([v.upper() for v in exp_fmts]))
                    print('Rasterization DPI: '+str(PNG_DPI))
                    print('Watch directory: '+self.watchdir)
                    print('Write directory: '+self.writedir)
                    files = get_files(self.watchdir,None);
                    lastmod = [os.path.getmtime(f) for f in files]
                    self.nf = False
                if timenow()>ltm + 0.25:
                    ltm = timenow();
                    # newfiles = [fn for fn in os.listdir(watchdir) if fn[-3:]=='svg']
                    newfiles = get_files(self.watchdir,None);
                    newlastmod = [0 for f in newfiles]
                    for ii in range(len(newfiles)):
                        try:
                            newlastmod[ii] = os.path.getmtime(newfiles[ii])
                        except FileNotFoundError:     
                            newlastmod[ii] = lastmod[ii]
                    
                    updatefiles = [];
                    if any([not(f in newfiles) for f in files]):
                        pass; # deleted files; 
                    elif any([not(n in files) for n in newfiles]):
                        updatefiles += [n for n in newfiles if not(n in files)]; # new files
                    elif any([newlastmod[ii]>lastmod[ii]+1 for ii in range(len(files))]): #updated files
                        updatefiles += [newfiles[ii] for ii in range(len(files)) if not(lastmod[ii]==newlastmod[ii])];
                    files = newfiles
                    lastmod = newlastmod
                    
                    if self.ea:  # export all
                        self.ea = False;
                        updatefiles = files
                    elif self.es:
                        self.es = False;
                        updatefiles = [self.selectedfile];
                    
                    # Exclude any files I made
                    for fn in genfiles:
                        if fn in updatefiles:
                            updatefiles.remove(fn)
                    
                    loopme = True; genfiles
                    while loopme:
                        for f in updatefiles:
                            # while not(self.stopped):
                            print('\nExporting '+f+'')
                            
                            outfile = joinmod(self.writedir,os.path.split(f)[1]);
                            if (reduce_images or text_to_paths) and any([f in exp_fmts for f in ['svg','pdf','emf','eps']]):
                                ppoutput = preprocessing(self.bfn,f,outfile)
                                tempoutputs = ppoutput[1]; tempdir = ppoutput[2];
                            else:
                                ppoutput = None
                                tempoutputs = []; tempdir = None;
                            
                            for fmt in exp_fmts:
                                finished, tf, myo = export_file(self.bfn,f,outfile,fmt,ppoutput=ppoutput);
                                if finished:
                                    genfiles.append(myo)
                                    genfiles = list(set(genfiles)); # unique values
                                    genfiles = [v for v in genfiles if v[-3:]=='svg']
                                tempoutputs += tf
                            
                            if not(DEBUG):
                                for t in list(set(tempoutputs)):
                                    os.remove(t);
                                if tempdir is not None:
                                    os.rmdir(tempdir);        
                            
                        loopme = (len(updatefiles)>0 and self.dm);
                    if len(updatefiles)>0:
                        print(promptstring)

        if self.threadID==2:
            self.ui = input(promptstring)
    def stop(self):
         self.stopped = True;

# Main loop
t1 = myThread(1);
t1.bfn = bfn;
t1.watchdir = watchdir;
t1.writedir = writedir;
# print('TEst')
# t1.bfn = Validate_Binary(t1.bfn);
# print('TEst')
if t1.watchdir is None or t1.writedir is None:
    t1.watchdir, t1.writedir = Get_Directories()

       
t1.start();
while t1.nf:  # wait until it's done initializing
    pass
t2 = myThread(2); t2.start();
keeprunning = True;
while keeprunning:
    if not(t2.is_alive()):
        if t2.ui in ['Q','q']:
            t1.stop();
            keeprunning = False
        elif t2.ui in ['D','d']:
            if hastkinter:
                try:
                    t1.watchdir, t1.writedir = Get_Directories()
                    t1.nf = True
                except:
                    pass
            t2 = myThread(2); t2.start();
        elif t2.ui in ['R','r']:
            PNG_DPI = int(input('Enter new rasterization DPI: '));
            t2 = myThread(2); t2.start();
        elif t2.ui in ['A','a']:
            t1.ea = True;
            t2 = myThread(2); t2.start();
        elif t2.ui in ['F','f']:
            if hastkinter:
                try:
                    t1.selectedfile = Get_File(t1.watchdir)
                    t1.es = True
                except:
                    pass
            t2 = myThread(2); t2.start();
        elif t2.ui in ['#']:
            t1.dm = True; # entering # starts an infinite export loop in the current dir
            t1.ea = True;
            t2 = myThread(2); t2.start();
        else:
            print('Invalid input!')
            t2 = myThread(2); t2.start();

# On macOS close the terminal we opened
# https://superuser.com/questions/158375/how-do-i-close-the-terminal-in-osx-from-the-command-line
if platform.system().lower()=='darwin':
   os.system('osascript -e \'tell application \"Terminal\" to close first window\' & exit');