import cv2 as cv
import time
import numpy as np
i = 0
while True:
    line_image = np.zeros((500,500,3),dtype='uint8')
    line_image[:] = 0,54,25
    cv.line(line_image,(0,250),(250,250),(20,20,45),thickness=2)#here the thickness cannot be filled or -1 use justpositive ok
    cv.putText(line_image,"Your device has been hacked",(50, 100), cv.FONT_HERSHEY_SIMPLEX,0.8, (0, 0, 255), 2,cv.LINE_AA)
    name = 'line'+str(i)
    cv.imshow(name,line_image)
    time.sleep(0.1)
    i+=1

    if cv.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break
    if(i>=30):
        break

cv.destroyAllWindows()
