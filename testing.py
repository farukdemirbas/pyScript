import cv2

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

cv2.imwrite(savepath, result)