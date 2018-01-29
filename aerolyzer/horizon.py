import sys
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from retrieve_image_data import RtrvData as Data

#def _is_sky(self, red, green, blue):
#	maxIndexRed = np.argmin(red)
#	maxIndexBlue = np.argmin(blue)
#	maxIndexGreen = np.argmin(green)

        #insert code to determine if range of max values is accepted as a sky

#	return True

# Create a mask
data    = Data("./images/img2.jpg")
img = data.get_rgb('./images/img2.jpg')
mask = np.zeros(img.shape[:2], np.uint8)
mask[0:(img.shape[0]/2), 0:img.shape[1]] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Create histograms with 16 bins in range 0-255
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],mask,[16],[0,255])
    plt.plot(histr,color = col)
    plt.xlim([0,16])
plt.show()
#hist_blue = cv2.calcHist([img],[0],mask,[16],[0,255]);
#hist_green = cv2.calcHist([img],[1],mask,[16],[0,255]);
#hist_red = cv2.calcHist([img],[2],mask,[16],[0,255]);
#plt.hist(hist_red); plt.show()
#plt.hist(hist_green); plt.show()
#plt.hist(hist_blue); plt.show()
#print hist_blue
#print hist_green
#print hist_red
#return self._is_sky(hist_blue, hist_green, hist_red)

#horizon()._testAnalyze("./images/")
			
