from horizon import is_sky
from os import listdir
from os.path import isfile, join
pics = [f for f in listdir("./images/good-images/") if isfile(join("./images/good-images/", f))]
good = 0
bad = 0
#is_sky("1484949766_27_557", "./images/good-images/1484949766_27_557.jpg")

for i in pics:
    print "./images/good-images/" + i
    if is_sky(i, "./images/good-images/" + i):
        good = good + 1
    else:
        bad = bad + 1

percent = float(float(good) / float(good+bad))*100.
print 'horizon detection is', percent, 'accurate.'

