import os
#import json
import shutil
import cv2
KPS = 1# Target frames Per Second
VIDEO_PATH = "C:\\Users\\aryuemaan\\Pictures\\Camera Roll\\Traffic_Light_After_Rain.mp4" # Change this in your computer
IMAGE_PATH = "C:\\Users\\aryuemaan\\Documents\\After rain images\\"
EXTENSION = ".jpg" # extension of the images
cap = cv2.VideoCapture(VIDEO_PATH) # reads the video.
fps = round(cap.get(cv2.CAP_PROP_FPS)) # computes the fps of the video.
print(fps) # prints the fps
# exit()
hop = round(fps / KPS) # the target fps rounded integer number.
curr_frame = 0 # initialise current frame
i = 0
while(True): # run infinite loop
    ret, frame = cap.read() # read the frame and ret shows if there is frame
    if frame is not None:
        frame = frame[0:1080, 0:1920] # resize the image in order to remove bonnet.
        if curr_frame % hop == 0: # if the current frame is set to the hop.
            print(i); # monitoring purpose
            name = IMAGE_PATH + "" + str(i) + EXTENSION # name of the image
            cv2.imwrite(name, frame) # write the frame to the directory
            i+=1
        curr_frame += 1 # increment of the current frame
    else:
        break # if no frame break the loop