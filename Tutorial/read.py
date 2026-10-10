import cv2 as cv

def readingPhotos():
    # without any flag
    img = cv.imread('Resources/Photos/Cat.jpg')
    # default version
    img2 = cv.imread('Resources/Photos/Cat.jpg', cv.IMREAD_UNCHANGED)
    # b&w
    img3 = cv.imread('Resources/Photos/Cat.jpg', cv.IMREAD_GRAYSCALE)
    # without Alpha Channel
    img4 = cv.imread('Resources/Photos/Cat.jpg', cv.IMREAD_COLOR)

    cv.imshow('Cat', img)
    cv.imshow('Cat2', img2)
    cv.imshow('Cat3', img3)
    cv.imshow('Cat4', img4)
    cv.waitKey(0)


def readingVideos():
    capture = cv.VideoCapture(0)  # for webcam, also use -1
    capture2 = cv.VideoCapture('Resources/Videos/dog.mp4')

    while True:
        # properly(boolean) controls whether frame reading properly
        # frame(matrix) contain all information picture have
        # .read() function has its own iterator
        properly, frame = capture2.read()
        cv.imshow('Video', frame)
        # waitkey is necessary, because of asynchron architecture
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    capture.release()
    # memory cleaning
    capture2.release()