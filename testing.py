""" import cv2

image1 = cv2.imread("C:/Users/faruk/Pictures/pp.jpg")
image2 = cv2.imread("C:/Users/faruk/Pictures/gris.jpeg")
savepath = "C:/Users/faruk/Desktop/pyScript/testing.jpg"

pt1 = (20, 40)
pt2 = (190, 400)
color = (145, 22, 65)

#result = cv2.arrowedLine(image1, pt1, pt2, color, 3)
#result = cv2.circle(image1, pt1, 5, color, 3)
#result = cv2.circle(image1, pt1, 5, color, 3)
#result = cv2.drawMarker(image1, pt1, color)
#result = cv2.HoughCircles(image1, cv2.HOUGH_GRADIENT, 1, 20)

cv2.imwrite(savepath, result) """

# Python program to illustrate  
# saving an operated video 
  
import cv2 
  
# This will return video from the first webcam on your computer. 
cap = cv2.VideoCapture(0)   
  
# Define the codec and create VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output1.avi', fourcc, 20.0, (640, 480)) 
  
# loop runs if capturing has been initialized.  
while(True): 
    # reads frames from a camera  
    # ret checks return at each frame 
    ret, frame = cap.read()  
  
    # Converts to HSV color space, OCV reads colors as BGR 
    # frame is converted to hsv 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
      
    # output the frame 
    out.write(hsv)  
      
    # The original input frame is shown in the window  
    #cv2.imshow('Original', frame) 
  
    # The window showing the operated video stream  
    #cv2.imshow('frame', hsv) 
  
      
    # Wait for 'a' key to stop the program  
    #if cv2.waitKey(1) & 0xFF == ord('a'): 
    #    break
  
# Close the window / Release webcam 
cap.release() 
  
# After we release our webcam, we also release the output 
out.release()  
  
# De-allocate any associated memory usage  
cv2.destroyAllWindows()