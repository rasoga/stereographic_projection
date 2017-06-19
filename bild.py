#!/usr/bin/python
#import Image, ImageDraw
from PIL import Image, ImageDraw
import math
import numpy as np

import progressbar

original_name = "test.jpg"
output_name = "yay.jpg"


inPic = Image.open(original_name)

# choose raduis by size
boxRad = np.round( 0.5 * min(inPic.width,inPic.height) ).astype(int)

# Define the two necessary rotation matrices
rotx = np.reshape([1, 0, 0,
                    0, 0, 1,
                    0, -1, 0], (3,3))
roty = np.reshape([0, 0, 1,
                     0, 1, 0,
                     -1, 0, 0], (3,3))
rotz = np.reshape([0, 1, 0,
                   -1, 0, 0,
                   0, 0, 1], (3,3))
rotations = [
  np.reshape([1, 0, 0,
              0, 1, 0,
              0, 0, 1], (3,3)),
  rotx,
  np.dot(rotx, rotx),
  np.dot(np.dot(np.transpose(rotx), rotz),rotz),
  np.dot(roty, rotz),
  np.transpose(np.dot(rotz,roty))
]

def findcoord(i,x,y, br = boxRad):
  pt = np.array([x - br, y - br, -br])
  return np.dot(rotations[i], pt)
  
def inBox(newCoord, boxRad):
  return newCoord[0] >= 0 and newCoord[0]<4*boxRad and newCoord[1] >= 0 and newCoord[1] < 4*boxRad

# Crop image to get a square
im = inPic.crop(
  [np.round(.5*inPic.size[0])-boxRad,
   np.round(.5*inPic.size[1])-boxRad,
   np.round(.5*inPic.size[0])+boxRad,
   np.round(.5*inPic.size[1])+boxRad])

im.save("crop.jpeg","JPEG")

print("Done cropping.")

# Get a pixel accessor.
pixels = im.load()

#define image
mResult = Image.new("RGB", (4*boxRad, 4*boxRad), "white")
draw = ImageDraw.Draw(mResult)

m2 = Image.new("RGB", (2*boxRad, 2*boxRad), "white")
d2 = ImageDraw.Draw(m2)

print("Start transformation.")

bar = progressbar.ProgressBar()
#1) compute coordinate of cube -> erstmal egal...einfach x,y auf 2 coord packen je seite
#2) normalize
#3) stereographic
for x in bar(range(boxRad*2)):
  for y in range(boxRad*2):
    px = pixels[x,y]
    d2.point([x, y], fill = px)
    for i in range(6):
      # Compute coordinates on one of the six sides of the cube
      # Afterwards project on unit sphere.
      ccoord = findcoord(i, x, y)
      normCoord = ccoord/np.linalg.norm(ccoord)
      
      #projection
      if normCoord[-1] == 1:#falls nordpol
        continue

      # stereographic projection
      newCoord = normCoord[:-1] / (1 - normCoord[-1]) * 2 * boxRad

      #shift to middle and round
      newCoord = np.round(newCoord + np.array([2*boxRad] * 2))
      
      if inBox(newCoord, boxRad): #alles, was noch im bild liegt malen
        draw.point(list(newCoord), fill = px)
        
draw.ellipse((boxRad,boxRad,3*boxRad,3*boxRad),outline=(255,0,0)) #referenz-Kreis
del draw

print("Transformation done.")

# Save file to output_name
mResult.save(output_name, "JPEG")
m2.save("blubb.jpg")
