import cv2 as cv

def rescaleVideo():
    def rescaleFrame(frame, scale):#images,videos, live videos
        # frame is a numpy ndarray type, so it has this type variables attributes
        # we must turn to integer because pixel number is a decimal numbers
        width = int(frame.shape[1] * scale)  # 1 is the width
        height = int(frame.shape[0] * scale)  # 0 is the height
        dimensions = (width, height)
        # INTER_AREA is a algorithm, learn this maan!!!!!
        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

    capture2 = cv.VideoCapture('Resources/Videos/dog.mp4')
    while True:
        properly, frame = capture2.read()
        frame_resized = rescaleFrame(frame, 0.75)
        cv.imshow('Video', frame)
        cv.imshow('Video_Resized', frame_resized)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    # memory cleaning
    capture2.release()


def rescalePhotos():
    def rescaleFrame(frame, scale):  # images,videos, live videos
        # frame is a numpy ndarray type, so it has this type variables attributes
        # we must turn to integer because pixel number is a decimal numbers
        width = int(frame.shape[1] * scale)  # 1 is the width
        height = int(frame.shape[0] * scale)  # 0 is the height
        dimensions = (width, height)
        # INTER_AREA is a algorithm, learn this maan!!!!!
        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

    img = cv.imread("Resources/Photos/cat.jpg")
    resized_image = rescaleFrame(img, 0.75)
    cv.imshow('Cat', img)
    cv.imshow('Resized', resized_image)
    cv.waitKey(0)


def resizeWebCam():
    global capture

    def changeRes(cap, width, height):
        # Live Video
        capture.set(3, width)
        capture.set(4, height)

    capture = cv.VideoCapture(0)
    changeRes(capture, 1024, 720)
    while True:
        properly, frame = capture.read()
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    # memory cleaning
    capture.release()