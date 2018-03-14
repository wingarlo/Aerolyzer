import cv2
import numpy as np
import aerosol
import time
import math
from retrieve_image_data import RtrvData


def test_all():
        testspassed  = 0
        numtests  = 0
        if(test_analyzeWavelength()==1):
                print "test_analyzeWavelength() passed\n"
                testspassed+=1
                numtests+=1
        else:
                numtests+=1
                print "test_analyzeWavelength() failed\n"
        if(test_readHazeLayer()==1):
                print "test_readHazeLayer() passed\n"
                testspassed+=1
                numtests+=1
        else:
                numtests+=1
                print "test_readHazeLayer() failed\n"



        print "Number of Tests passed "+ str(testspassed) +"/"+str(numtests)+"\n"


def test_analyzeWavelength():
        rand = np.random.random() *1000
        wavelength = 300.0
        print aerosol.analyzeWavelength(wavelength)
        return 1
def gen_hsvtestlist():
        randsize = int(((np.random.random() *10000)%200)**2)
        testList = []
        print "Randsize: "+str(randsize)+"\n"
        for i in range(randsize):
                randh = (np.random.random() *1000)%180
                rands = (np.random.random() *1000)%255
                randv = (np.random.random() *1000)%255
                testList.append([randh,rands,randv])
        print "testlist done"
        return testList,randsize
def test_readHazeLayer():
        test = RtrvData("./images/img6.jpg")
        t2 = time.time()
        testList,numPixels = test.get_rgb("./images/img6.jpg")
        t3 = time.time()
        timeRandoms = t3-t2
        print "time gen_hsvtestlist(): "+ str(timeRandoms)
        t0 = time.time()
        print aerosol.readHazeLayer(testList)
        t1 = time.time()
        total_n = t1-t0
        print "readHazeLayer runtime: "+ str(total_n)
        speedpp = total_n/numPixels
        print "readHazeLayer speed per pixel: "+ str(speedpp)
        return 1
