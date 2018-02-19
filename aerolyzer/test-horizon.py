from horizon import is_sky
import numpy as np
from os import listdir
from os.path import isfile, join
pics = [f for f in listdir("./images/good-images/") if isfile(join("./images/good-images/", f))]
good = 0
bad = 0

#is_sky("a","./images/good-images/1484949760_19_2615.jpg")

for i in pics:
    print "./images/good-images/" + i
    is_sky(i, "./images/good-images/" + i)
    #    good = good + 1
    #else:
    #    bad = bad + 1

#percent = float(float(good) / float(good+bad))*100.
#print 'valid horizon detection is', percent, 'accurate.'


#for i in pics:
    #print "./images/false-imgs/" + i
    #if is_sky(i, "./images/false-imgs/" + i):
    #    good = good + 1
    #else:
    #    bad = bad + 1

#percent = float(float(bad) / float(good+bad))*100.
#print 'invalid horizon detection is', percent, 'accurate.'

