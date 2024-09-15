import cv2
import numpy as np
image=cv2.imread('./VK.jpeg')
if image is None:
	print("Error:Unable to read te image")
else:
	heigth,width=image.shape[:2]
	angle=90
	scale_x=0.5
	scale_y=0.5
	offset_x=100
	offset_y=50
	rotation_matrix=cv2.getRotationMatrix2D((width/2,heigth/2),angle,1)
	rotation_image=cv2.warpAffine(image,rotation_matrix,(width,heigth))
	scaled_image=cv2.resize(image,None,fx=scale_x,fy=scale_y,interpolation =cv2.INTER_LINEAR)
	translation_matrix=np.float32([[1,0,offset_x],[0,1,offset_y]])
	translation_image=cv2.warpAffine(image,translation_matrix,(width,heigth))
	cv2.imshow('Original Image',image)
	cv2.imshow('Rotated Image',rotation_image)
	cv2.imshow('Scaled Image',scaled_image)
	cv2.imshow('Translated Image',translation_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
