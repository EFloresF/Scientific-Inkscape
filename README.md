# Academic-Inkscape: Extensions for plot resizing and manipulation
This repository contains two Inkscape extensions designed for plot modification. The first, Scale Plots, can be used to change the size or aspect ratio of a plot without modifying its text. It is not as flexible as doing the same modification in the original plotting program, but is still much easier than doing the same thing manually. The second, Flatten Plots, is a helper extension that eliminates much of the structure generated by common vector graphics plotting programs. 

# Installation
Install using the instructions provided here: https://inkscape.org/gallery/=extension/. Copy these files into the directory listed at Edit > Preferences > System: User extensions. After a restart of Inkscape, the group extensions will be available under Extensions > Academic.

# Scale Plots
When dealing with vector graphics generated by plotting programs like Matlab and matplotlib, resizing plots can be a pain. When assembling subfigures one generally wants to resize the lines and data of a plot, but leave text and stroke widths unaffected. This is best done in the original program, but sometimes one just wants to do a quick modification.

For most plots, Scale Plots generates acceptable scalings with little effort. The plot should be flattened using Flatten Plots first, as objects in groups will be left alone by the scaling. The entire selection is scaled, and then text and groups are unscaled. The extension attempts to maintain the distance between axes and labels/tick labels by assigning a plot area—a bounding box is calculated that contains the largest horizontal and vertical lines, and anything outside is assumed to be a label. If your plot's axes do not have lines, temporarily add them to define a plot area. If you would like to ensure that an object remains unscaled, simply place it in a group.

Scale Plots also has a "Matching Mode," which matches the plot area to the size of the first object you select. This can be convenient when assembling subfigures, as you can match the size of one plot to another or to a template rectangle.
            
# Other features
1. If "Auto tick correct" is enabled, the extension assumes that any small horizontal or vertical lines near the edges of the plot area are ticks, and automatically unscales them.
2. If a layer name is put into the "Scale-free layer" option, any elements on that layer will be unscaled as well. This is most useful for markers, which should not be scaled.
