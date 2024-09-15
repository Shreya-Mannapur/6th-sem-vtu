import cv2
image=cv2.imread('/home/jss/image.jpg')
if image is None:
	print("Error:Unable to read the image")
else:
	gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	_,binary_image=cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
	contours,_=cv2.findContours(binary_image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	contoured_image=cv2.drawContours(image.copy(),contours,-1,(0,255,0),2)
	cv2.imshow('Contoured Image',contoured_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
