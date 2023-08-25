#This is the script without the need of a FFmpeg installation, pure OpenCV
import cv2
import numpy as np
from time import time
import socket
from goprocam import GoProCamera

gpCam = GoProCamera.GoPro()
gpCam.livestream("start")
cap = cv2.VideoCapture("udp://10.5.5.1:8554")
while True:
    nmat, frame = cap.read()
    cv2.imshow("GoPro OpenCV", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
        '''
    if time() - t >= 2.5:
        #sock.sendto("_GPHD_:0:0:2:0.000000\n".encode(), ("10.5.5.9", 8554))
        sock.sendto("_GPHD_:0:0:2:0.000000\n".encode(), ("10.5.5.9", 8554))
        t=time()
    '''
# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
