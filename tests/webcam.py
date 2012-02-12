import cv
import Image

cv.NamedWindow("camera", 1)
capture = cv.CaptureFromCAM(0)
while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    print cv.WaitKey(10)
    if cv.WaitKey(10) == 27:
        break
    
    if cv.WaitKey(1) == 13:
        cv.SaveImage("WEBCAM_windows_and_python.jpg", img)
        break 
    
cv.DestroyWindow("camera")
