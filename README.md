# Scientific Inkscape: Extensions for figure editing and resizing
Scientific Inkscape is a set of Inkscape extensions designed for editing scientific figures, making common tasks easier.

1. **Scale Plots**: Changes the size or aspect ratio of a plot without modifying its text and ticks. Especially useful for assembling multi-panel figures.
2. **Flatten Plots**: A utility that eliminates much of the structure generated by common plot generation programs. With it, most plots are far easier to edit.
3. **The Homogenizer**: Quickly sets uniform fonts, font sizes, and stroke widths in a selection.
4. **Combine by Color**: An extension that fuses paths of the same color and style together into a single path. Handy for speeding up operations on plots with thousands of similar elements, like markers. 
5. **Auto-Exporter**: Automatically exports SVG files in a directory and keeps them updated.
6. **Text Ghoster**: Adds a semi-transparent background to text so that it can be overlayed with data.

All were written by [David Burghoff](https://dburghoff.com) at the University of Notre Dame. If you find it useful, tell your collegaues!

# Installation
You must have the latest release version of Inkscape (1.1), and the extensions should be installed using the instructions provided [here](https://inkscape.org/gallery/=extension/). Download all of these files, then copy them into the directory listed at Edit > Preferences > System: User extensions. After a restart of Inkscape, the group extensions will be available under Extensions > Scientific.

# Scale Plots
When dealing with vector graphics generated by plotting environments like Matlab and Matplotlib, resizing plots after the plot has been generated can be difficult. Generally, one wants to resize the lines and data of a plot while leaving text, ticks, and stroke widths unaffected. This is best done in the original program, but may be time-consuming.

For most plots, Scale Plots generates acceptable scalings with little effort. Lines and data are scaled while text and ticks are merely repositioned. The extension attempts to maintain the distance between axes and labels/tick labels by assigning a _plot area_—a bounding box that is calculated from the largest horizontal and vertical lines. Anything outside is assumed to be a label. (If your plot's axes do not have lines, temporarily add a framed box to define a plot area.)

![Scale Plots example](https://github.com/burghoff/Academic-Inkscape/blob/main/examples/Scale%20Plots%20example.svg)

To use:

1. Run Flatten Plots on your plot to remove groups generated by the PDF/EPS/SVG exporting process. 
2. Place any objects that you wish to remain unscaled in a group.
3. Select the elements of your plot and run Scale Plots.

Scale Plots has three modes. In Scaling Mode, the plot is scaled by a constant factor. In Matching Mode, the plot area is made to match the size of the first object you select. This can be convenient when assembling subfigures, as it allows you to match the size of one plot to another plot or to a template rectangle. In Correction Mode, a plot that has already been (badly) manually scaled will be corrected. This is so you can manually drag the figure (see below).
<br><p align="center"><img src="https://github.com/burghoff/Academic-Inkscape/blob/main/examples/Correction_mode.gif" width="75%"></img></p>

## Advanced options
1. If "Auto tick correct" is enabled, the extension assumes that any small horizontal or vertical lines near the edges of the plot area are ticks, and automatically leaves them unscaled.
2. If a layer name or group ID is put into the "Scale-free elements" option, any elements on that layer will remain unscaled. This is basically the same thing as putting an object in a group, but can be easier if there are many such objects (e.g, if your plot has markers).

# Flatten Plots
Flatten Plots is a utility that makes it easier to edit plots are exported from common plotting programs and imported into Inkscape, as well as figures imported from papers.
1. *Deep ungroup*: The Scale Plots utility uses grouping to determine when objects are to be kept together, so a deep ungroup is typically needed to remove any existing groupings initially. It also unlinks any clones.
2. *Apply text fixes*: Applies a series of fixes to text described below (particularly useful for PDF/EPS text).
3. *Remove white rectangles*: Removes any rectangles that have white fill and no stroke. Mostly for removing a plot's background.

### Text fixes
<ol>
<li><i>Split distant text and lines</i>: It is often the case that the PDF/EPS printing process generates text implemented as a single text object. For example, all of the x-axis ticks might be one object, all of the y-axis ticks might be another, and the title and labels may be another. Internally, each letter is positioned independently. This looks fine, but causes issues when trying to scale or do anything nontrivial.</li>
<li><i>Merge nearby text</i>: The opposite can also occur: text that should be one line is split into multiple objects. This option reverses that.
<li><i>Remove manual kerning</i>: Text in PDFs is typically kerned—its letters are positioned individually, so if you try to edit it you will get strange results. This option reverses that, although the tradeoff is that text may be slightly repositioned.</li>
<li><i>Merge superscripts and subscripts</i>: Detect likely subscripts and superscripts, replacing them with native SVG versions.</li>
<li><i>Replace missing fonts</i>: Useful for imported documents whose original fonts are not installed on the current machine.</li></ol>

# The Homogenizer
The Homogenizer is a utility that can set all fonts, font sizes, and stroke widths in a selection to the same value. It also removes any text or path distortions. This is most useful when assembling sub-figures, as it allows you to ensure that the whole figure has a uniform look. 
<p align="center"><img src="https://github.com/burghoff/Academic-Inkscape/blob/main/examples/Homogenizer.svg" alt="drawing" ></img></p>

# Combine by Color
If you have used Inkscape for editing plots with thousands of elements, you have probably found that it behaves sluggishly. Often, this can be solved by combining paths of the same color together into a single path, but when your plot has multiple curves then you have to select the elements belonging to different curves separately. Combine by Color simplifies this, automatically fusing paths of the same style together. Not only does this tend to improve responsiveness, but typically it will also reduce the file size of the output.

Note: If you subsequently run Scale Plots on a path generated by Combine by Color, Scale Plots can treat the merged sub-paths independently—just specify the path ID as a Scale-free element.

# Auto-Exporter
When you are saving figures, you would generally like to export them whenever you save. The Auto-Exporter does this automatically: you specify a directory that the program monitors, and whenever any SVGs are changed, it automatically converts them to the formats you specify. Just select (a) the formats you would like to export, (b) what directory you would like it to watch, and (c) where you would like it to put the exports. Any rasterization is done at 600 DPI and is given a white background.

# Text Ghoster
Placing text labels can sometimes be difficult for dense or small plots. The Text Ghoster adds a blurry semi-transparent background to text, allowing the text to be legible without obscuring the data.

<p align="center"><img src="https://github.com/burghoff/Academic-Inkscape/blob/main/examples/Ghoster.svg" alt="drawing" ></img></p>
