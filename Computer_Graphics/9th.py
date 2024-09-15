import cv2
import numpy as np
image=cv2.imread('./VK.jpeg')
if image is None:
	print("Error")
else:
	gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	blurred_image=cv2.GaussianBlur(gray_image,(5,5),0)
	edges=cv2.Canny(blurred_image,50,150)
	cv2.imshow('Edges',edges)
	laplacian=cv2.Laplacian(blurred_image,cv2.CV_64F)
	laplacian=np.uint8(np.absolute(laplacian))
	cv2.imshow('Texture(Laplacian)',laplacian)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
