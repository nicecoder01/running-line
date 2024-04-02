import cv2 
import numpy as np
vid = cv2.VideoWriter('myvideo.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 24, (100, 100))
frame = np.zeros((100, 100, 3), np.uint8)
duration=3
text=input()
x=50
for i in range(0,duration*24):
  frame.fill(0)
  cv2.putText(frame, text, (x,50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,128,0))
  x=x-len(text)//2
  vid.write(frame)
vid.release()
