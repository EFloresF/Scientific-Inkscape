# Academic-Inkscape: Extensions for plot resizing and manipulation
This repository contains two Inkscape extensions designed for plot modification. The primary extension, Scale Plots, changes the size or aspect ratio of a plot without modifying its text and ticks. The secondary extension, Flatten Plots, is a utility extension that eliminates much of the structure generated by common vector graphics plotting programs.

# Installation
Install using the instructions provided [here](https://inkscape.org/gallery/=extension/). Copy the repository files into the directory listed at Edit > Preferences > System: User extensions. After a restart of Inkscape, the group extensions will be available under Extensions > Academic.

# Scale Plots
When dealing with vector graphics generated by plotting programs like Matlab and matplotlib, resizing plots can be a pain. Generally, one wants to resize the lines and data of a plot while leaving text and stroke widths unaffected. This is best done in the original program, but sometimes one just wants to do a quick modification.

For most plots, Scale Plots generates acceptable scalings with little effort. Lines and data are scaled while text and ticks are merely repositioned. The extension attempts to maintain the distance between axes and labels/tick labels by assigning a _plot area_—a bounding box that is calculated from the largest horizontal and vertical lines. Anything outside is assumed to be a label. (If your plot's axes do not have lines, temporarily add them to define a plot area.)

![Scale Plots example](https://raw.githubusercontent.com/burghoff/Academic-Inkscape/1c57fd4af4fb6509ca4570a854412a4546b15256/examples/Scale%20Plots%20example.svg)

To use:

1. Run Flatten Plots on your plot to remove any unwanted structure generated by the PDF/EPS/SVG exporting process. 
2. Place any objects that you wish to remain unscaled in a group
3. Select the elements of your plot and run Scale Plots.

Scale Plots has two modes. In Scaling Mode, the plot is scaled by a constant factor. In Matching Mode, the plot area is made to match the size of the first object you select. This can be convenient when assembling subfigures, as it allows you to match the size of one plot to another plot or to a template rectangle.
            
# Other features
1. If "Auto tick correct" is enabled, the extension assumes that any small horizontal or vertical lines near the edges of the plot area are ticks, and automatically unscales them.
2. If a layer name is put into the "Scale-free layer" option, any elements on that layer will be unscaled as well. This is most useful for markers, which should not be scaled.
