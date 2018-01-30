import sys
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from retrieve_image_data import RtrvData as Data

# Create a mask
data    = Data("./phones/droidx/2011-08-20_01-04-19_612.jpg")
img = data.get_rgb('./phones/droidx/2011-08-20_01-04-19_612.jpg')
tags = data.get_exif('./phones/droidx/2011-08-20_01-04-19_612.jpg',True,True)
mask = np.zeros(img.shape[:2], np.uint8)
mask[0:(img.shape[0]/2), 0:img.shape[1]] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Create histograms with 16 bins in range 0-255
color = ('b','g','r')
#for i,col in enumerate(color):
#    histr = cv2.calcHist([img],[i],mask,[255],[0,255])
#    plt.plot(histr,color = col)
#    plt.xlim([0,255])
#    print np.argmax(histr)
#plt.show()
dimx = tags['exif exifimagewidth']
dimy = tags['exif exifimagelength']
b,g,r = cv2.split(img)
largest = [0,0]
it = dimy / 200
for i in range(dimy/4,(dimy/4)*3,it):
	ravg = (sum(r[i]) / float(len(r[i])))
	gavg = (sum(g[i]) / float(len(g[i])))
	bavg = (sum(b[i]) / float(len(b[i])))
	avg = (ravg + gavg + bavg) / 3
	pravg = (sum(r[i-it]) / float(len(r[i-it])))
	pgavg = (sum(g[i-it]) / float(len(g[i-it])))
	pbavg = (sum(b[i-it]) / float(len(b[i-it])))
	pavg = (pravg + pgavg + pbavg) / 3
	diff = pavg - avg
	if diff > largest[0]:
		largest = [diff,i-(it/2)]
print largest
sky = img[0:largest[1],0:dimx]
cv2.imwrite('./cropped.jpg',sky)
