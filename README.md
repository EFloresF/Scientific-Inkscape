# Academic-Inkscape: Extensions for plot resizing and manipulation
This repository contains two Inkscape extensions designed for plot modification. The main one, Scale Plots, changes the size or aspect ratio of a plot without modifying its text and ticks. The second one, Flatten Plots, is a utility that eliminates much of the structure generated by common vector graphics plotting programs. (Written by [David Burghoff](https://dburghoff.com) at the University of Notre Dame.) In addition, it contains the Auto-Exporter, a program that will automatically detect changes in a directory's SVG files and export them to various formats. 

# Installation
Install using the instructions provided [here](https://inkscape.org/gallery/=extension/). Download all of these files, then copy them into the directory listed at Edit > Preferences > System: User extensions. After a restart of Inkscape, the group extensions will be available under Extensions > Academic. These extensions will only work in the latest release version of Inkscape (1.0.2).

# Scale Plots
When dealing with vector graphics generated by plotting environments like Matlab and Matplotlib, resizing plots after the plot has been generated can be difficult. Generally, one wants to resize the lines and data of a plot while leaving text, ticks, and stroke widths unaffected. This is best done in the original program, but precludes quick modification.

For most plots, Scale Plots generates acceptable scalings with little effort. Lines and data are scaled while text and ticks are merely repositioned. The extension attempts to maintain the distance between axes and labels/tick labels by assigning a _plot area_—a bounding box that is calculated from the largest horizontal and vertical lines. Anything outside is assumed to be a label. (If your plot's axes do not have lines, temporarily add a box to define a plot area.)

![Scale Plots example](https://github.com/burghoff/Academic-Inkscape/blob/main/examples/Scale%20Plots%20example.svg)

To use:

1. Run Flatten Plots on your plot to remove structure generated by the PDF/EPS/SVG exporting process. 
2. Place any objects that you wish to remain unscaled in a group.
3. Select the elements of your plot and run Scale Plots.

Scale Plots has two modes. In Scaling Mode, the plot is scaled by a constant factor. In Matching Mode, the plot area is made to match the size of the first object you select. This can be convenient when assembling subfigures, as it allows you to match the size of one plot to another plot or to a template rectangle.
            
## Advanced options
1. If "Auto tick correct" is enabled, the extension assumes that any small horizontal or vertical lines near the edges of the plot area are ticks, and automatically leaves them unscaled.
2. If a layer name is put into the "Scale-free layer" option, any elements on that layer will remain unscaled. This is basically the same thing as putting an object in a group, but can be easier if there are many such objects (e.g, if your plot has markers).

# Flatten Plots
Flatten Plots is a useful utility for eliminating many of the annoyances that arise when dealing with imported plots.
1. *Deep ungroup*: The Scale Plots utility uses grouping to determine when objects are to be kept together, so a deep ungroup is typically needed to remove any existing groupings initially. While there is a standalone Deep Ungroup extension built in to Inkscape, it is somewhat buggy—the version in Inkscape 1.0.2 cannot ungroup *any* of the plots in the provided test file.
2. *Apply text fixes*: Applies a series of fixes to text described below.
3. *Remove white rectangles*: Removes any rectangles that have white fill and no stroke. Mostly for removing a plot's background.

### Text fixes
<ol>
<li><i>Split distant text</i>: Depending on the renderer, it is often the case that the PDF/EPS printing process generates text implemented as a single text object. For example, all of the x-axis ticks might be one object, all of the y-axis ticks might be another, and the title and labels may be another. Internally, each letter is positioned independently. This looks fine, but causes issues when trying to scale or do anything nontrivial.
<br><p align="center"><img src="https://github.com/burghoff/Academic-Inkscape/blob/main/examples/Split_distant_draw.png" alt="drawing" ></img></p></li>
<li><i>Repair shattered text</i>: Similarly, text in PDFs is often 'shattered'—its letters are positioned individually, so if you try to edit it you will get strange results. This option reverses that, although the tradeoff is that text may be slightly repositioned.
<br><p align="center"><img src="https://github.com/burghoff/Academic-Inkscape/blob/main/examples/Repair_shattered_draw.png" alt="drawing" ></img></p></li>
<li><i>Replace missing fonts</i>: Useful for imported documents whose original fonts are not installed on the current machine.</li></ol>

# Auto-Exporter
The Auto-Exporter is not an extension, it is a Python script meant to be run in the background (as a daemon). If you frequently export SVGs to other formats, this program does it automatically for you. It will do so for all files in a directory and in multiple formats. Just select (a) the location where the Inkscape binary is installed, (b) what directory you would like it to watch, and (c) where you would like it to put the exports.
