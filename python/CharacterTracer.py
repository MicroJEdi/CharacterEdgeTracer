from PIL import Image
from PIL import ImageFilter
import math


maxError = 6.5
picWidth = 0
picHeight = 0
outputPic = None
img = None
imgRGB = None


def parseSymbol():
	global picWidth, picHeight, imgRGB, img
	picWidth, picHeight = img.size
	for x in range(1,picWidth-1):
		for y in range(1, picHeight-1):
			r,g,b = img.getpixel((x, y))
			if(r+b+g > 450):
				xTemp = x
				yTemp = y
				while(yTemp < picHeight-1 and xTemp < picWidth-1):
					rx,gx,bx = img.getpixel((xTemp, yTemp+1))
					if(rx+bx+gx > 450):
						img.putpixel((xTemp,yTemp), (240, 240, 0))
						yTemp += 1
					else:
						rx,gx,bx = img.getpixel((xTemp+1, yTemp+1))
						if(rx+bx+gx > 450):
							img.putpixel((xTemp,yTemp), (240, 0, 0))
							yTemp += 1
							xTemp += 1
						else:
							break
				while(yTemp > 0 and xTemp < picWidth-1):
					rx,gx,bx = img.getpixel((xTemp, yTemp-1))
					if(rx+bx+gx > 450):
						img.putpixel((xTemp,yTemp), (240, 240, 0))
						yTemp -= 1
					else:
						rx,gx,bx = img.getpixel((xTemp+1, yTemp-1))
						if(rx+bx+gx > 450):
							img.putpixel((xTemp,yTemp), (0, 0, 240))
							yTemp -= 1
							xTemp += 1
						else:
							break
	img.save("circuitTraced.JPEG", "JPEG")
#end parseSymbol


def initializeRGB(fileName):
	global picWidth, picHeight, imgRGB, img, outputPic
	img = Image.open(fileName)
	picWidth, picHeight = img.size
	imgEnhanced = img.convert('RGB')
	imgEnhanced = imgEnhanced.filter(ImageFilter.BLUR)
	imgEnhanced = imgEnhanced.filter(ImageFilter.BLUR)
	imgEnhanced = imgEnhanced.filter(ImageFilter.BLUR)
	imgRGB  = imgEnhanced.convert('RGB')
	outputPic = (picHeight)*[(picWidth)*[0]]
#end initializeRGB


def segmentRGB():
	global numColors, picWidth, picHeight, outputPic, maxError, imgRGB, img
	for y in range(1, picHeight-1):
		for x in range(1,picWidth-1):
			r,g,b = imgRGB.getpixel((x, y))
			outputPic[y][x] = 0

			val1 = 0
			val2 = 0
			val3 = 0

			rx,gx,bx = imgRGB.getpixel((x-1, y-1))
			error = (abs(r-rx)+abs(g-gx)+abs(b-bx))/3
			if( error < maxError ):
				outputPic[y][x] += 1

			rx,gx,bx = imgRGB.getpixel((x, y-1))
			error = (abs(r-rx)+abs(g-gx)+abs(b-bx))/3
			if( error < maxError ):
				outputPic[y][x] += 2

			rx,gx,bx = imgRGB.getpixel((x+1, y-1))
			error = (abs(r-rx)+abs(g-gx)+abs(b-bx))/3
			if( error < maxError ):
				outputPic[y][x] += 4

			rx,gx,bx = imgRGB.getpixel((x+1, y))
			error = (abs(r-rx)+abs(g-gx)+abs(b-bx))/3
			if( error < maxError ):
				outputPic[y][x] += 8

			rx,gx,bx = imgRGB.getpixel((x+1, y+1))
			error = (abs(r-rx)+abs(g-gx)+abs(b-bx))/3
			if( error < maxError ):
				outputPic[y][x] += 16

			rx,gx,bx = imgRGB.getpixel((x, y+1))
			error = (abs(r-rx)+abs(g-gx)+abs(b-bx))/3
			if( error < maxError ):
				outputPic[y][x] += 32

			rx,gx,bx = imgRGB.getpixel((x-1, y+1))
			error = (abs(r-rx)+abs(g-gx)+abs(b-bx))/3
			if( error < maxError ):
				outputPic[y][x] += 64

			rx,gx,bx = imgRGB.getpixel((x-1, y))
			error = (abs(r-rx)+abs(g-gx)+abs(b-bx))/3
			if( error < maxError ):
				outputPic[y][x] += 128

			if(outputPic[y][x] == 255):
				img.putpixel((x,y), (0, 0, 0))
			if(outputPic[y][x] < 255):
				img.putpixel((x,y), (255, 255, 255))
	img.save("circuitBlackAndWhite.JPEG", "JPEG")
#end segmentRGB


def main(fileName):
	print "start"
	initializeRGB(fileName)
	segmentRGB()
	parseSymbol()
	print "complete"
#end main

main("circuit.jpg")
