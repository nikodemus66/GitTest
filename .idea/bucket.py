__author__ = 'Dominic'

#from SimpleCV import *
from SimpleCV import Camera, Image, DrawingLayer, Color
from math import atan, degrees

BUCKET_WIDTH_CM = 37
#DISTANC_CAM_BUCKET_CM = 185
threshLvls = [17,25,30,40,60,80,100,120,140,160,-1]
bucketDistance = 150

#input = input("Abstand zum Kuebel eingeben(0 = 150cm):") != 0
#if input != 0:
#    bucketDistance = input

cam = Camera()

def findBucket(img, aThreshLvl=0):
    if len(threshLvls) == aThreshLvl:
        return
    binPicture = img.binarize(thresh=threshLvls[aThreshLvl])
    blobs = binPicture.findBlobs(minsize=17000, maxsize=24000)
    if blobs:
        return blobs[len(blobs)-1]
    else:
        newThresh = aThreshLvl + 1
        return findBucket(img, newThresh)

def calcAngle(bucketWidthPixel, pictureWidth, bucketXPosition):
    pixelCmRatio = bucketWidthPixel / BUCKET_WIDTH_CM
    bucketDistanzFromMid = ((pictureWidth/2)-bucketXPosition)
    print "position X in CM: ", bucketDistanzFromMid/pixelCmRatio
    angelRadians =  atan(bucketDistanzFromMid/(bucketDistance*pixelCmRatio))
    return round(degrees(angelRadians),1)

def drawLines(picture):
    drawlayer = DrawingLayer((picture.width, picture.height))
    lineX = 0
    while(lineX < picture.width):
        lineX += 50
        drawlayer.line((lineX,0),(lineX,picture.height),Color.RED,1,True)
    picture.addDrawingLayer(drawlayer)

while True:
    picture = cam.getImage()
    drawLines(picture)
    blob = findBucket(picture)
    if blob:
        picture.drawRectangle(blob.minRectX(),blob.minRectY(),blob.minRectWidth(),blob.minRectHeight(),Color.BLUE)
        print "angle: ",calcAngle(blob.minRectWidth(),picture.width,blob.minRectX())
    else:
        print "nothing found"
    picture.show()