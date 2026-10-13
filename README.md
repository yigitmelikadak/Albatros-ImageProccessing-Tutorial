# Albatros-ImageProccessing-Tutorial
My Journey in Learning Image Processing

October 10,
I create environment and repo.

October 11,

1.30 AM <br>
I learned: <br>
.imread(directory,flag) refers to read pictures properties <br> 
flags = { cv.IMREAD_UNCHANGED <br>
          cv.IMREAD_GRAYSCALE <br>
          cv.IMREAD_COLOR <br>
          } <br>
.imshow(windowTitle,.imread) refers to visualize picture according to .imread <br> 
.VideoCapture(source) refers to choose source to read data <br>
source = { <br>
           -1 refers to webcam <br>
            0 refers to webcam<br>
            1 refers to second cam<br>
            or we can use<br>
            directory<br>
            }<br>
.read(booelan,frame) it has its own iterator, so for loop is not necessarily.<br>
booelan check is there problem when video is playing frame by frame<br>
frame holds all the information a picture have<br>
waitkey(ms) for waiting, it may necessary due to asynchron architecture<br> 
ms == 0 => infinite time<br>
.release() is used  for releasing memory<br> 
  prevent memory leaks and other stuff<br>
I have problem when:<br>
  understanding .read() <br>  
  
October 12, resizing and rescaling <br>
October 13, draw shapes and text, convert gray, gaussian blur, edge cascade, dilate, erode, resize, translate, rotate, flip, finding contours with two ways, color spaces and convert formats, split-merge color channels