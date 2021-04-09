# STORM_GUI


This is the Speer Lab STORM Analysis Application (beta). 


## How to Run? 

* Run `main.py` through command `python main.py`
* This will load the GUI 


## Functionality

* Pipeline for processing STORM data
 * Test fitting parameters on small portion of STORM data prior to running full analysis 
 * Multifit scmos analysis on all STORM and bead movies 
 * XY alignment for images in physical sections 
 * Z alignment and elastic registration


(see additional readme docs for more information) 


## Instructions 

### Visualizing DAX Files 

To load a DAX file, you can either drag and drop a file to the movie-viewer or simply load one using the 
`Load Movie` button at the top left. 

To move through the frames: 

* Press '.' to step forward one frame 
* Press ',' to step backward one frame 
* Press 'l' to step forward 200 frames 
* Press 'k' to step backward 200 frames 
* Press 'Home' to go to beginning of movie 
* Press 'End' to go to end of movie 

To change the contrast, adjust the vertical contrast bar to desired value. 

Additionally, you can load localizations which can be overlayed on top of the movie frame.

### Evaluating Fitting Parameters 

First select the desired channels for analysis through the checkboxes next to "Storm Channels". To modify the XML files, click on "Set Test Parameters" and for each desired channel, select the corresponding XML file. Doing so should auto-complete the fields in the form. Once you are done, press "Update XMLs". 

You can choose the how many processes to run by either modifying the field directly or using the slider. 


### SCMOS Batch Analysis 

First you can select the start and end frames for each of the desired channels by pressing the "Set Frame Range" button and completing the form. Once you are done, make sure you select the desired alignment channel through the checkboxes near "Alignment Channels". Then, select the number of processes and run "Multifit Analysis" 

# Known Bugs and Issues 

* Currently the DAX Visualization breaks when you go past 10000 frames 
* No way of choosing number of frames - temporary fix is it to go to "keyPressEvent()" method in `main.py` and replace 200 with selected value. 

