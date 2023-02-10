# Inkscape Auto-Exporter, by David Burghoff
# Service that checks a folder for changes in svg files, and then exports them
# automatically to another folder in multiple formats.

DEBUG = False
WHILESLEEP = 0.25;

PORTNUMBER = 5001
try:
    import sys, platform, subprocess, os, threading, datetime, time, copy, pickle, re
    import numpy as np
    
    try:
        import gi
        gi.require_version('Gtk', '3.0')
        from gi.repository import Gtk
        guitype = 'gtk'
    except:
        try:
            import tkinter as tk
            from tkinter import filedialog
            guitype = 'tkinter'
        except:
            guitype = 'terminal'
    
    from dhelpers import si_tmp
    aes = si_tmp(filename='si_ppe_settings.p')
    with open(aes, "rb") as f:
        input_options = pickle.load(f)
    os.remove(aes)
    
    # Need to silence output in Mac or else doesn't run outside shell
    # silenced = platform.system().lower()=="darwin" and not(input_options.inshell)
    # if silenced:
    #     os.system(
    #         "osascript -e 'tell application \"Terminal\" to close first window' & exit"
    #     )
    #     sys.stdout = open(os.devnull, 'w')
    #     sys.stderr = open(os.devnull, 'w')
    # silenced = False
    # def print(*args):
    #     if not(silenced):
    #         print(args)
    
    # Clear out leftover temp files from the last time we ran
    # mypath = os.path.dirname(os.path.realpath(sys.argv[0]))
    lftover_tmp = si_tmp(filename='si_ae_leftovertemp.p')
    # lftover_tmp = os.path.join(os.path.dirname(os.path.realpath(__file__)),'tmp','"si_ae_leftovertemp.p"')
    leftover_temps = [];
    if os.path.exists(lftover_tmp):
        f = open(lftover_tmp, "rb")
        leftover_temps = pickle.load(f)
        f.close()
        os.remove(lftover_tmp)
        for tf in leftover_temps:
            if os.path.exists(tf):
                try:
                    os.rmdir(tf)
                    leftover_temps.remove(tf)
                except PermissionError:
                    pass
            else:
                leftover_temps.remove(tf)
                
    bfn       = input_options.inkscape_bfn
    sys.path += input_options.syspath
    
    import inkex
    from inkex import Vector2d, Transform
    import dhelpers as dh
    
    import sys
    import webbrowser

    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    sys.path += [os.path.join(current_script_directory,'packages')]
    
    import urllib
    import pathlib
    def file_uri_to_path(file_uri, path_class=pathlib.PurePath):
        # https://stackoverflow.com/questions/5977576/is-there-a-convenient-way-to-map-a-file-uri-to-os-path
        """
        This function returns a pathlib.PurePath object for the supplied file URI.
    
        :param str file_uri: The file URI ...
        :param class path_class: The type of path in the file_uri. By default it uses
            the system specific path pathlib.PurePath, to force a specific type of path
            pass pathlib.PureWindowsPath or pathlib.PurePosixPath
        :returns: the pathlib.PurePath object
        :rtype: pathlib.PurePath
        """
        windows_path = isinstance(path_class(),pathlib.PureWindowsPath)
        file_uri_parsed = urllib.parse.urlparse(file_uri)
        file_uri_path_unquoted = urllib.parse.unquote(file_uri_parsed.path)
        if windows_path and file_uri_path_unquoted.startswith("/"):
            result = path_class(file_uri_path_unquoted[1:])
        else:
            result = path_class(file_uri_path_unquoted)
        if result.is_absolute() == False:
            raise ValueError("Invalid file uri {} : resulting path {} not absolute".format(
                file_uri, result))
        return result
    
    def Make_Flask_App(static_folder):
        from flask import Flask, request, url_for, jsonify, send_from_directory
        app = Flask(__name__)
        
        global folder_dict
        folder_dict = dict();
        
        @app.route('/images/<folder>/<path:path>')
        def send_image(folder,path):
            global folder_dict
            return send_from_directory(os.path.abspath(folder_dict[folder]), path)
            # response = send_from_directory(os.path.abspath(folder_dict[folder]), path)
            # response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            # response.headers["Pragma"] = "no-cache"
            # response.headers["Expires"] = "0"
            # return response

        @app.route("/")
        def index():
            global temp_dir
            gloc = os.path.join(temp_dir,"Gallery.html");
            with open(gloc, "rb") as f:
                gallery = f.read();
                
                global fileuris
                nnames = [];
                for v in fileuris:
                    svg_file = file_uri_to_path(v)
                    folder, file = os.path.split(svg_file)
                    
                    global folder_dict
                    if folder not in folder_dict.values():
                        k = os.path.split(temp_dir)[-1]+'-dir'+str(len(folder_dict));
                        folder_dict[k] = folder
                    else:
                        k = next(key for key, value in folder_dict.items() if value == folder)
                    nnames.append(url_for('send_image', path=file, folder=k))
                new_string = gallery.replace(b'var imgAddresses = '+bytes(str(fileuris),'utf-8'),
                                             b'var imgAddresses = '+bytes(str(nnames),'utf-8'))
                # print(gallery)
                # print(bytes('hello\n'*1000,'utf-8'))
                # print(gallery)
                return new_string
                # return '<img src="{}">'.format(url_for('send_image', path='image2.svg'))
        @app.route("/stop")
        def stop():
            func = request.environ.get('werkzeug.server.shutdown')
            if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
            func()
            return "Server shutting down..."
        
        @app.route("/process", methods=["GET"])
        def process():
            param = request.args.get("param")
            # svg_file = os.path.normpath(param).strip('file:\\');
            # svg_file = re.sub("^file:\\\\", "", os.path.normpath(param))
            svg_file = file_uri_to_path(param)
            if svg_file is not None:
                print('Opening'+str(svg_file))
                subprocess.run([bfn, svg_file]);
            return f"The parameter received is: {param}"
        
        @app.route('/check_for_refresh')
        def check_for_refresh():
            global refreshapp, lastupdate
            if refreshapp:
                refreshapp = False
                lastupdate = time.time();
            return jsonify(lastupdate=lastupdate)
            
        def run_flask():
            # app.static_folder = static_folder
            app.run(port = PORTNUMBER)
        from threading import Thread
        thread = Thread(target=run_flask)
        thread.start()
        return app
    
    
    global temp_dir
    temp_dir = si_tmp(dirbase='ppe');
    
    # global temp_dir
    # import tempfile
    # temp_dir = tempfile.TemporaryDirectory().name
    
    import os
    import zipfile
    import shutil
    import subprocess
    import tempfile
    
    def make_svg_display(svg_filenames,thumbnails,header,slidenums,islinked):
        import os
        IMAGE_WIDTH = 200;
        IMAGE_HEIGHT = IMAGE_WIDTH*0.7;
    
        # Create the HTML file
        global temp_dir
        gloc = os.path.join(temp_dir,"Gallery.html");
        with open(gloc, "w") as file:
        # Write the HTML header
            file.write('<html translate="no">\n')
            
            # Define the CSS styles
            css_styles = """
            <style>
            div.gallery {
              margin: 5px;
              border: 1px solid #ccc;
              float: none;
              width: IMAGE_WIDTHpx;
              display: inline-block;
            }
            
            div.gallery:hover {
              border: 1px solid #777;
            }
            
            div.gallery img {
              object-fit: contain;
              width: IMAGE_WIDTHpx;
              height: IMAGE_HEIGHTpx;
            }
            
            div.desc {
              padding: 15px;
              text-align: center;
            }
            </style>
            """
            css_styles = css_styles.replace('IMAGE_WIDTH', str(IMAGE_WIDTH))
            css_styles = css_styles.replace('IMAGE_HEIGHT',str(IMAGE_HEIGHT))
            # Create the string with the <head>, <style>, and </style> tags
            meta = "<meta name='google' content='notranslate'>\n";
            title = "<title>SVG Gallery</title>\n"
            string = "<head>{0}{1}{2}</head>".format(css_styles,meta,title)
            file.write(string)
            file.write("<body>\n")
            
            global fileuris
            fileuris = []; ii=0;
            file.write('<h1>'+header+'</h1>\n<div class="serverdown" style="color: #e41a1cff;"></div>')
            # Loop through the SVG filenames and write an img tag for each one
            for ii, svg in enumerate(svg_filenames):
                gallery = """
                <div class="gallery">
                  <a target="_blank" href="#">
                    <img src="#" alt="" id='img{2}'>
                  </a>
                  <div class="desc">{4}<a href="http://localhost:{3}/process?param={0}" class="open">Open in Inkscape</a></div>
                </div>
                """
                myloc = "file://" + svg;
                
                import pathlib
                myloc = pathlib.Path(svg).as_uri()
                tnloc = pathlib.Path(thumbnails[ii]).as_uri()
                if slidenums is not None:
                    label = 'Slide {0}'.format(slidenums[ii])+(' (linked)' if islinked[ii] else '')+'<br>'
                else:
                    label = os.path.split(svg)[-1]+'<br>';
                file.write(gallery.format(myloc,os.path.split(svg)[-1],ii,str(PORTNUMBER),label))
                fileuris.append(tnloc);
            
            #<br><a href="http://localhost:5000/stop" id="stop_link">Stop Server</a>
            file.write("""
               <script>
                document.querySelectorAll("a.open").forEach(function(link) {
                    link.addEventListener("click", function(event){
                        event.preventDefault();
                        var xhr = new XMLHttpRequest();
                        xhr.open("GET", this.href, true);
                        xhr.send();
                    });
                });
                </script>
                """)
            
            script = """
            <script>
            var imgAddresses = replacemenow;
            var imgloaded = imgAddresses.map(() => false);
    
            function loadImage(counter) {
              // Break out if no more images
              if (counter==imgAddresses.length) { return; }
            
              // Grab an image obj
              var I = document.getElementById("img"+counter);
            
              // Monitor load or error events, moving on to next image in either case
              try {
                  I.onload = I.onerror = function() {checkRun(counter);}
                  I.src = imgAddresses[counter];
                  I.parentNode.href = imgAddresses[counter];
              } catch (error) {
              }
            }
            const Nshow = 2100;
            var currentRun = 0;
            var waitingOn = 0;
            function checkRun(cval) {
                imgloaded[cval]=true;
                if (imgloaded.slice(0, currentRun*Nshow).some(element => element === true) & cval-(cval%Nshow)==Nshow*waitingOn) {
                    queueRun();
                }
            }
            function queueRun() {
                for (let i = currentRun*Nshow; i < (currentRun+1)*Nshow; i++) {
                  loadImage(i);
                }
                waitingOn = currentRun;
                currentRun++;
                // console.log(currentRun)
                // console.log(imgAddresses.length)
            }
            queueRun();
            
            //for (let i = 0; i < imgAddresses.length; i++) {
            //  loadImage(i);
            //  }
            
            var mylastupdate = Date.now() / 1000;
            setInterval(function(){
                var xhr = new XMLHttpRequest();
                xhr.open('GET', '/check_for_refresh');
                xhr.onload = function() {
                    if (xhr.status === 200) {
                        var response = JSON.parse(xhr.responseText);
                        if (response.lastupdate > mylastupdate) {
                            location.reload();
                        }
                    }
                };
                xhr.onerror = function() {
                document.querySelector('.serverdown').innerHTML = "Server is not running.";
                };
                xhr.send();
            }, 1000);
            </script>
            """
            # global replacemenowval
            # replacemenowval = tofill
            script = script.replace('replacemenow',str(fileuris))
            file.write(script)
            
            # Write the HTML footer
            file.write("</body>\n")
            file.write("</html>\n")
        # return 
        

        import webbrowser, pathlib
        print('Gallery: '+pathlib.Path(gloc).as_uri())
        # webbrowser.open(pathlib.Path(gloc).as_uri())
        # webbrowser.open("http://localhost:{}".format(str(PORTNUMBER)))
    
    # def unzip_ppt_open_svg(filename):

    class WatcherThread(threading.Thread):
        # A thread that generates an SVG gallery of files, then watches
        # it for changes
        def __init__(self, file_or_folder):
            threading.Thread.__init__(self)
            # self.threadID = threadID
            self.fof = file_or_folder
            self.stopped = False

        def get_image_slidenums(self,dirin):
            import os
            import xml.etree.ElementTree as ET
            relsdir = os.path.join(dirin,'ppt/slides/_rels')
            numslides = len(os.listdir(relsdir))
            slide_filenames = [];
            for slide_num in range(1,numslides+1):
                rels_file = f"ppt/slides/_rels/slide{slide_num}.xml.rels"
                tree = ET.parse(os.path.join(dirin,rels_file))
                root = tree.getroot()
                image_filenames = []
                for elem in root.iter("{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"):
                    if elem.attrib["Type"] == "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image":
                        image_filenames.append(elem.attrib["Target"])
                slide_filenames.append(image_filenames)
            slide_lookup = {}
            for index, filenames in enumerate(slide_filenames):
                for filename in filenames:
                    slide_lookup[filename] = slide_lookup.get(filename, []) + [index + 1]
            return slide_lookup


        def run_on_fof(self):
            print("Running on file:", self.fof)
            global temp_dir
            
            numc = sum([f.startswith('contents') for f in os.listdir(temp_dir)])
            contents = os.path.join(temp_dir,'contents'+str(numc))
            def get_svgs(dirin):
                svg_filenames = []
                for file in os.listdir(dirin):
                  if file.endswith(".svg") or file.endswith(".emf"):
                    svg_filenames.append(os.path.join(dirin,file))
                svg_filenames.sort()
                return svg_filenames

            if os.path.isfile(self.fof):
                # Unzip the ppt file to the temp directory
                with zipfile.ZipFile(self.fof, 'r') as zip_ref:
                    zip_ref.extractall(contents)
                ppt_media_dir = os.path.join(contents, 'ppt', 'media')
                print(ppt_media_dir)
                self.files = get_svgs(ppt_media_dir);
                self.slidenums = self.get_image_slidenums(contents)
                
                # Add linked images to self.files
                linked = [str(file_uri_to_path(k)) for k in self.slidenums.keys() if 'file:' in k];
                self.files += linked;
                self.slidenums = {os.path.join(contents,'ppt','media',os.path.basename(k)) \
                                  if 'file:' not in k else str(file_uri_to_path(k)) : v \
                                      for k,v in self.slidenums.items()}
                
                # Sort the files by slide number and make slidenums a corresponding list
                # Duplicates filenames if on multiple slides
                new_files = []
                new_slidenums = []
                for file in self.files:
                    slides = self.slidenums.get(file, [float('inf')])
                    for slide in slides:
                        new_files.append(file)
                        new_slidenums.append(slide)
                new_files_and_slidenums = sorted(zip(new_files, new_slidenums), key=lambda x: (x[1], x[0]))
                self.files, self.slidenums = zip(*new_files_and_slidenums)
                self.slidenums = [v if v!=float('inf') else '?' for v in self.slidenums]
                self.islinked = [f in linked for f in self.files]

                # print(self.slidenums)
                # print(self.slidenums)
                # self.files.sort(key=lambda x: (min(self.slidenums.get(x, [float('inf')])), x))
                self.thumbnails = copy.copy(self.files)
                self.header = self.fof
                print("Temp dir: "+temp_dir)
            elif os.path.isdir(self.fof):
                self.files = get_svgs(self.fof);
                self.thumbnails = copy.copy(self.files)
                self.header = self.fof
                self.slidenums = None
                self.islinked = None
                
                
            tndir = os.path.join(temp_dir,'thumbnails')
            if not os.path.exists(tndir):
                os.makedirs(tndir)
            numtns = len(os.listdir(tndir))
            tns = [];
            for f in self.files:
                if f.endswith('.emf'):
                    tnpng = os.path.join(tndir,str(numtns)+'.png')
                    numtns+=1
                    print(tnpng)
                    tns.append(tnpng)
                else:
                    tns.append(f)
            self.thumbnails = tns

                
            make_svg_display(self.files,self.thumbnails,self.header,self.slidenums,self.islinked)
            
            global myapp, refreshapp
            if myapp is None:
                myapp = Make_Flask_App(temp_dir);
                webbrowser.open("http://localhost:{}".format(str(PORTNUMBER)))
            else:
                refreshapp = True
            self.convert_emfs()
            
            
        def convert_emfs(self):
            # Spawn a thread to convert all the EMFs to PNGs
            def overwrite_output(filein,fileout):
                import hashlib
                with open(f, "rb") as file:
                    file_content = file.read()
                    hashed = hashlib.sha256(file_content).hexdigest()
                global converted_files
                if hashed not in converted_files:
                    notdone = True
                    while notdone:
                        try:
                            if os.path.exists(fileout):
                                os.remove(fileout)
                            args = [bfn,"--export-area-drawing","--export-background","#ffffff","--export-background-opacity",
                                "1.0","--export-dpi",str(300),"--export-filename",fileout,filein,]
                            dh.subprocess_repeat(args)
                            notdone = False
                        except:
                            pass
                    global refreshapp
                    refreshapp = True
                    converted_files[hashed] = fileout
                else:
                    import shutil
                    shutil.copy2(converted_files[hashed], fileout)


            from threading import Thread
            threads = []
            for ii, f in enumerate(self.files):
                if f.endswith('.emf'):
                    print('Making thumbnail '+self.thumbnails[ii])
                    thread = Thread(target=overwrite_output, args=(f,self.thumbnails[ii]))
                    threads.append(thread)
                    while len([t for t in threads if t.is_alive()])>10:
                        time.sleep(0.1)
                    thread.start()
                        

        def run(self):
            self.run_on_fof()
            
            def get_modtimes():
                modtimes = dict()
                if os.path.isfile(self.fof):
                    modtimes[self.fof]  = os.path.getmtime(self.fof)
                elif os.path.isdir(self.fof):
                    fs = []
                    for f in os.scandir(self.fof):
                        if f.name.endswith(".svg") or f.name.endswith(".emf"):
                            fs.append(os.path.join(os.path.abspath(self.fof), f.name))
                    for f in fs:
                        modtimes[f] = os.path.getmtime(f);
                return modtimes
            
            lmts = get_modtimes();
            while not(self.stopped):
                time.sleep(1)
                mts = get_modtimes();
                if lmts!=mts:
                    self.run_on_fof()
                lmts = mts
            

    global myapp, refreshapp, converted_files
    myapp = None
    refreshapp = False
    converted_files = dict()
    lastupdate = time.time();
    watcher_threads = [];
    def process_selection(file):
        for wt in watcher_threads:
            wt.stopped = True
        wt = WatcherThread(file)
        wt.start()
        watcher_threads.append(wt)
      
    def quitnow():
        import requests
        requests.get('http://localhost:{}/stop'.format(str(PORTNUMBER)))  # kill Flask app
        
        for wt in watcher_threads:
            wt.stopped = True
        
        global temp_dir
        attempts = 0;
        while os.path.exists(temp_dir) and attempts<5:
            shutil.rmtree(temp_dir)
            attempts += 1
            time.sleep(5)
        
        pid = os.getpid()
        import signal
        os.kill(pid, signal.SIGINT) # or signal.SIGTERM
        
        
    if guitype=='gtk':            
        import gi
        gi.require_version('Gtk', '3.0')
        from gi.repository import Gtk, GdkPixbuf
        
        class HelloWorldWindow(Gtk.Window):
            def __init__(self):
                Gtk.Window.__init__(self, title="Powerpoint SVG Extractor")
                self.set_default_size(400, -1)  # set width to 400 pixels, height can be automatic
                self.set_position(Gtk.WindowPosition.CENTER)
                
                self.selected_file_label = Gtk.TextView()
                self.selected_file_label.set_editable(False)
                self.selected_file_label.set_wrap_mode(Gtk.WrapMode.CHAR)
                self.selected_file_label.get_buffer().set_text('No file selected.')
        
                # Adding a scrolled window to the TextView
                self.scrolled_window = Gtk.ScrolledWindow()
                self.scrolled_window.set_size_request(400, 200)
                self.scrolled_window.set_hexpand(True)
                self.scrolled_window.set_vexpand(True)
                self.scrolled_window.add(self.selected_file_label)
                            
                # Adding an Image widget to display the SVG
                # pixbuf = GdkPixbuf.Pixbuf.new_from_file('test.svg')
                # width, height = pixbuf.get_width(), pixbuf.get_height()
                # scale = min(100/width, 100/height)
                # pixbuf = pixbuf.scale_simple(int(width*scale), int(height*scale), GdkPixbuf.InterpType.BILINEAR)
                # self.svg_image = Gtk.Image()
                # self.svg_image.set_from_pixbuf(pixbuf)
                
                self.containing_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
                self.containing_box.set_valign(Gtk.Align.CENTER)
                self.containing_box.set_margin_top(20)
                self.containing_box.set_margin_bottom(20)
                self.containing_box.pack_start(self.scrolled_window, True, True, 0)
                # self.containing_box.pack_start(self.svg_image, False, False, 0)
        
                self.file_button = Gtk.Button(label="Select File")
                self.file_button.connect("clicked", self.on_file_button_clicked)
                
                self.folder_button = Gtk.Button(label="Select Folder")
                self.folder_button.connect("clicked", self.on_folder_button_clicked)
                
                self.exit_button = Gtk.Button(label="Exit")
                self.exit_button.connect("clicked", self.on_button_clicked)
            
                        
                self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
                self.box.pack_start(self.containing_box, True, True, 0)
                self.box.pack_start(self.file_button, False, False, 0)
                self.box.pack_start(self.folder_button, False, False, 0)
                self.box.pack_start(self.exit_button, False, False, 0)
                self.add(self.box)
                
                
            def print_text(self, text):
                buffer = self.selected_file_label.get_buffer()
                start, end = buffer.get_bounds()
                if buffer.get_text(start, end, False)=='No file selected.':
                    buffer.set_text('')
                buffer.insert(buffer.get_end_iter(), text+'\n')
                end_iter = buffer.get_end_iter()
                buffer.move_mark(buffer.get_insert(), end_iter)
                self.selected_file_label.scroll_to_mark(buffer.get_insert(), 0, True, 0, 0)

            def on_button_clicked(self, widget):
                print("Hello World")
                self.destroy()
                
            def on_file_button_clicked(self, widget):
                native = Gtk.FileChooserNative.new("Please choose a file", self, Gtk.FileChooserAction.OPEN, None, None)
                filter_ppt = Gtk.FileFilter()
                filter_ppt.set_name("Powerpoint files")
                filter_ppt.add_pattern("*.ppt")
                filter_ppt.add_pattern("*.pptx")
                native.add_filter(filter_ppt)
                response = native.run()
                if response == Gtk.ResponseType.ACCEPT:
                    selected_file = native.get_filename()
                    self.print_text(selected_file)
                    process_selection(selected_file)
                native.destroy()
                
            def on_folder_button_clicked(self, widget):
                native = Gtk.FileChooserNative.new("Please choose a file or directory", self, Gtk.FileChooserAction.SELECT_FOLDER, None, None)
                response = native.run()
                if response == Gtk.ResponseType.ACCEPT:
                    selected_file = native.get_filename()
                    self.print_text(selected_file)
                    process_selection(selected_file)
                native.destroy()
                
                
        win = HelloWorldWindow()
        win.set_keep_above(True)
        # win.connect("destroy", quitnow)
        def quit_and_close(self):
            quitnow()
            Gtk.main_quit();
        win.connect("destroy", quit_and_close)
        win.show_all()
        win.set_keep_above(False)
        Gtk.main()
    elif guitype=='tkinter':
        root = tk.Tk()
        root.title("Powerpoint SVG Extractor")
        root.attributes("-topmost", True)
        root.wm_minsize(width=350, height=-1)
        def open_file():
            file = filedialog.askopenfilename()
            file_label.config(text=file)
            process_selection(file)
        def end_program():
            print('Quitting')
            root.destroy()
            quitnow();
        file_label = tk.Label(root, text="No file selected.")
        file_label.pack()
        select_button = tk.Button(root, text="Select File", command=open_file)
        select_button.pack()
        end_button = tk.Button(root, text="End Program", command=end_program)
        end_button.pack()
        root.protocol("WM_DELETE_WINDOW", end_program)
        root.mainloop()

except:
    import traceback
    print("An error has occurred:")
    print(traceback.format_exc())
    import time
    time.sleep(10);
        
    # try:
    #     import gi
    #     gi.require_version('Gtk', '3.0')
    #     from gi.repository import Gtk
        
        # class FileSelector(Gtk.Window):
        
        #     def __init__(self):
        #         Gtk.Window.__init__(self, title="File Selector")
        #         self.set_border_width(10)
        
        #         self.file_label = Gtk.Label(label="No file selected.")
        #         self.add(self.file_label)
        
        #         select_button = Gtk.Button(label="Select File")
        #         select_button.connect("clicked", self.on_open_clicked)
        #         self.add(select_button)
        
        #         end_button = Gtk.Button(label="End Program")
        #         end_button.connect("clicked", self.on_end_clicked)
        #         self.add(end_button)
        
        #     def on_open_clicked(self, widget):
        #         dialog = Gtk.FileChooserDialog("Please choose a file", self,
        #             Gtk.FileChooserAction.OPEN,
        #             (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
        #               Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        
        #         self.add_filters(dialog)
        #         response = dialog.run()
        
        #         if response == Gtk.ResponseType.OK:
        #             file = dialog.get_filename()
        #             self.file_label.set_label(file)
        #             # file = 'Presentation12.pptx'
        #             process_selection(file)
        #         elif response == Gtk.ResponseType.CANCEL:
        #             print("Cancel clicked")
        
        #         dialog.destroy()
        
        #     def on_end_clicked(self, widget):
        #         Gtk.main_quit()
        #         import requests
        #         requests.get('http://localhost:5000/stop') # kill Flask app
        
        #     def add_filters(self, dialog):
        #         filter_text = Gtk.FileFilter()
        #         filter_text.set_name("Text files")
        #         filter_text.add_mime_type("text/plain")
        #         dialog.add_filter(filter_text)
        
        #         filter_py = Gtk.FileFilter()
        #         filter_py.set_name("Python files")
        #         filter_py.add_mime_type("text/x-python")
        #         dialog.add_filter(filter_py)
    # except:
    #     import traceback
    #     print("An error has occurred:")
    #     print(traceback.format_exc())
        
    #     import time
    #     # import flask
    # print('Running?')
    # time.sleep(10);