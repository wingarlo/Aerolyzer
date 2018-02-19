import sys
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from retrieve_image_data import RtrvData as Data


def is_sky(a, path):
    #print path
    # Create a mask
    data = Data(path)
    img = data.get_rgb(path)
    tags = data.get_exif(path, True, True)
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[0:(img.shape[0] / 2), 0:img.shape[1]] = 255
    masked_img = cv2.bitwise_and(img, img, mask = mask)

    # Create histograms with 16 bins in range 0-255
    color = ('b', 'g', 'r')
    b, g, r = cv2.split(img)
    dimy, dimx = img.shape[:2]

    largest = [0, 0]
    it = dimy / 200 #iterations = total number of rows(pixels) / 200
    for i in range(dimy / 6, (dimy / 6) * 5, it):   #only looking at the middle half of the image
        ravg = (sum(r[i]) / float(len(r[i])))
        gavg = (sum(g[i]) / float(len(g[i])))
        bavg = (sum(b[i]) / float(len(b[i])))
        avg = (ravg + gavg + bavg) / 3
        pravg = (sum(r[i - it]) / float(len(r[i - it])))
        pgavg = (sum(g[i - it]) / float(len(g[i - it])))
        pbavg = (sum(b[i - it]) / float(len(b[i - it])))
        pavg = (pravg + pgavg + pbavg) / 3
        diff = pavg - avg
        if diff > largest[0]:   #only getting the largest intensity drop.
            largest = [diff,i-(it/2)]
    #print largest
    if largest[0] >= 0:
        sky = img[0:largest[1], 0:dimx]#cropping out landscape
        #cv2.imwrite('./' + a + '-cropped.jpg', sky)
        h1 = sky[0:(sky.shape[0] / 2), 0:dimx]#top half of sky
        h2 = sky[(sky.shape[0] / 2):(sky.shape[0]), 0:dimx]#bottom half
        #cv2.imwrite('./' + a + '-croppedt.jpg', h1)
        #cv2.imwrite('./' + a + '-croppedb.jpg', h2)
        mask1 = np.zeros(h1.shape[:2], np.uint8)
        mask1[0:(h1.shape[0] / 2), 0:h1.shape[1]] = 255
	hist1 = [0,0,0]
	hist2 = [0,0,0]
        max1 = [0,0,0]
        max2 = [0,0,0]
        for i,col in enumerate(color):
            hist1[i] = cv2.calcHist([h1], [i], mask1, [255], [0, 255])
            #print hist1[i]
            #plt.plot(hist1[i], color = col)
            #plt.xlim([0,255])
            print "Top half", color[i], "max", float(np.argmax(hist1[i][6:250]))/255.
            max1[i] = np.argmax(hist1[i][6:250])

        mask2 = np.zeros(h2.shape[:2], np.uint8)
        mask2[0:(h2.shape[0] / 2), 0:h2.shape[1]] = 255
        for j,col in enumerate(color):
            hist2[j] = cv2.calcHist([h2], [j], mask2, [255], [0, 255])
            #print hist2[j][20:]
            #plt.plot(hist2[j], color = col)
            #plt.xlim([0, 255])
            print "Bottom half", color[j], "max", float(np.argmax(hist2[j][6:250]))/255.
            max2[j] = np.argmax(hist2[j][6:250])
        #if max2[2] >= max1[2]-10:
        #X = np.array([hist1[0],hist1[1],hist1[2],hist2[0],hist2[1],hist2[2]])
        #if (sum(max2)) >= (sum(max1)):
            #cv2.imwrite('./' + a + '-cropped.jpg', sky)
        return True

    return False
