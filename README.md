# Albatros-ImageProccessing-Tutorial
My Journey in Learning Image Processing

October 10,
I create environment and repo.

October 11,

1.30 AM 
I learned:
.imread(directory,flag) refers to read pictures properties 
flags = { cv.IMREAD_UNCHANGED
          cv.IMREAD_GRAYSCALE
          cv.IMREAD_COLOR
          }
.imshow(windowTitle,.imread) refers to visualize picture according to .imread 
.VideoCapture(source) refers to choose source to read data
source = {
           -1 refers to webcam
            0 refers to webcam
            1 refers to second cam
            or we can use
            directory
            }
.read(booelan,frame) it has its own iterator, so for loop is not necessarily.
booelan check is there problem when video is playing frame by frame
frame holds all the information a picture have
waitkey(ms) for waiting, it may necessary due to asynchron architecture 
ms == 0 => infinite time
.release() is used  for releasing memory 
  prevent memory leaks and other stuff
  
I have problem when:
  understanding .read()   
