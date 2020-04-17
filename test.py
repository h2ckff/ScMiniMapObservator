file = open("ModuleVersions.json", 'w')
modules = {}

import os
import time
import winsound

import sys
modules['Python'] = dict([('version', sys.version_info)])

import json
modules['json'] = dict([('version', json.__version__)])

import numpy
modules['numpy'] = dict([('version', numpy.__version__)])

import PIL
modules['PIL'] = dict([('version', PIL.__version__)])
from PIL import Image

import mss
modules['mss'] = dict([('version', mss.__version__)])
from mss.windows import MSS as mss

import ctypes
modules['ctypes'] = dict([('version', ctypes.__version__)])

json.dump(modules, file, indent=4, sort_keys=True)
file.close()

def ScreenGrab(bbox):

	im=mss().grab(bbox)
	im=Image.frombytes("RGB", im.size, im.bgra, "raw", "BGRX")
	return im

def GetOutline(im,bbox):
	tempList = colorList
	for y in range (0,222):
		for x in range (0,262):
			if im.getpixel((x,y)) == (0, 49, 191):
				colorList[y*262+x] = 1
			else:
				colorList[y*262+x] = 0
	if tempList == colorList:
		return False
	else:
		return True

def Main(xbbox,ybbox,colorList):

	sct = mss()
	bbox={'width':int(xbbox),'left':int(27),'height':int(ybbox),'top':int(826)}

	while 1==1:
		im=ScreenGrab(bbox)

		if GetOutline(im,bbox):
			print("jest")
			frequency = 2500
			duration = 1000
			winsound.Beep(frequency, duration)
			time.sleep(5)



if __name__ == "__main__":
	colorList = []
	for i in range(0, 58164):
		colorList.append(i)
	xbbox = 262
	ybbox = 222
	Main(xbbox,ybbox,colorList)
