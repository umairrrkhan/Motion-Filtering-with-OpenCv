import cv2 as cv

video = cv.VideoCapture('Messi Incredible Goal vs Athletic Bilbao - English Commentary.mp4')

output_video = cv.VideoWriter('output_video 2.mp4', cv.VideoWriter_fourcc(*'mp4v'), 30, (0, 0), isColor=False)

# video = cv.videocapture(0)  you can use this code for camera dont need to download the video

subtractor = cv.createBackgroundSubtractorMOG2(20 , 50)

while True:
    ret , frame = video.read()

    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask',mask)
        if cv.waitKey(5) == ord('x'):
            break
    else:
        video= cv.VideoCapture('Messi Incredible Goal vs Athletic Bilbao - English Commentary.mp4')

cv.destroyAllWindows()
video.release()
output_video.release()


