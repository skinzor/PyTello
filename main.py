from DroneController import Tello
from FaceDetection import detect_face
import cv2 as cv

kpX = 0.15
kpY = 0.3

tello = Tello()

bat = tello.query_battery()

tello.takeoff()
tello.move_up(10)
        
while True:
    
    frame = tello.get_frame_read().frame  # capturing frame from drone 
    
    diff_x, diff_y, width = detect_face(frame)
    
    cv.imshow("drone", frame)             
    
    controlX = diff_x * kpX
    controlY = diff_y * kpY
    
    if (width < 150):
        controlPitch = 20
    elif (width > 200):
        controlPitch = -20
    else:
        controlPitch = 0
        
    tello.send_rc_control(0, controlPitch, int(-controlY), int(controlX))
    
    if cv.waitKey(1) & 0xFF == ord('q'):  # quit from script
        tello.streamoff()
        tello.land()
        cv.destroyAllWindows()
        break