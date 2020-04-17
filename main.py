import time
import winsound
import numpy
import PIL
from PIL import Image
import mss
from mss.windows import MSS as mss

xbbox = 262
ybbox = 222
bbox={'width':int(xbbox),'left':int(27),'height':int(ybbox),'top':int(826)}

def Ping():
	print("ping")
	frequency = 2500
	duration = 1000
	winsound.Beep(frequency, duration)
	time.sleep(5)

def ScreenGrab():
	im=mss().grab(bbox)
	im=Image.frombytes("RGB", im.size, im.bgra, "raw", "BGRX")
	return im

def ImageInspect(im):
    for y in range (0,ybbox):
        for x in range (0,xbbox):
            if im.getpixel((x,y)) == (0, 49, 191):
                return True
                break
    return False

def Main():
	while 1==1:
		im = ScreenGrab()
		if ImageInspect(im):
			Ping()

if __name__ == "__main__":
	Main()
