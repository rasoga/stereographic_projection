import Image, ImageDraw
import math
import numpy as np

original_name="test.jpg"
output_name="yay.jpg"



inPic = Image.open(original_name)


boxRad = 100
##choose raduis by size
boxRad = np.round( 0.5 * min(inPic.size[0],inPic.size[1]) )
boxRad = boxRad.astype(int)

edges = [np.array([-boxRad,-boxRad,boxRad]),\
np.array([boxRad,-boxRad,boxRad]),\
np.array([boxRad,boxRad,boxRad]),\
np.array([-boxRad,boxRad,boxRad]),\
np.array([-boxRad,-boxRad,boxRad]),\
np.array([boxRad,boxRad,-boxRad])]

def findcoord(i,x,y):
  if i==0:
    return edges[0]+np.array([x,0,-y])
  if i==1:
    return edges[1]+np.array([0,x,-y])
  if i==2:
    return edges[2]+np.array([-x,0,-y])
  if i==3:
    return edges[3]+np.array([0,-x,-y])
  if i==4:
    return edges[4]+np.array([y,x,0])
  if i==5:
    return edges[5]+np.array([-y,-x,0])
    
#im = Image.new("RGB", (512, 512), "white")

im = inPic.crop([np.round(.5*inPic.size[0])-boxRad,np.round(.5*inPic.size[1])-boxRad,np.round(.5*inPic.size[0])+boxRad,np.round(.5*inPic.size[1])+boxRad])

im.save("crop.jpeg","JPEG")

#make cube in an array
cube = [0]*6
for i in range(0,6):#6 sides, then x and y
  cube[i] = [0]*boxRad*2
  for x in range(0,boxRad*2):
    cube[i][x] = [0]*boxRad*2
    for y in range(0,boxRad*2):
      cube[i][x][y] = im.getpixel((x,y))

#define image
mResult = Image.new("RGB", (4*boxRad, 4*boxRad), "white")

draw = ImageDraw.Draw(mResult)

#1) compute coordinate of cube -> erstmal egal...einfach x,y auf 2 coord packen je seite
#2) normalize
#3) stereogtraphic
for i in range(0,6):
  for x in range(0,boxRad*2):
    for y in range(0,boxRad*2):
      #coords
      ccoord = findcoord(i,x,y)
      normCoord = ccoord/np.linalg.norm(ccoord)
      #projection
      if normCoord[2] == 1:#falls nordpol
        continue
      newCoord = np.array([normCoord[0]/(1-normCoord[2]),normCoord[1]/(1-normCoord[2])])*boxRad #in x,y #PROJECTION and scale up for visibility

      #shift to middle
      newCoord = newCoord + np.array([2*boxRad,2*boxRad])
      
      #round for image
      newCoord = np.round(newCoord)
      if newCoord[0] >= 0 and newCoord[0]<4*boxRad and newCoord[1] >= 0 and newCoord[1] < 4*boxRad:#alles, was noch im bild liegt malen
        #print(cube[i][x][y])
        draw.point([newCoord[0],newCoord[1]],fill=cube[i][x][y])
        
draw.ellipse((boxRad,boxRad,3*boxRad,3*boxRad),outline=(255,0,0)) #referenz-Kreis
del draw

# write to stdout
mResult.save(output_name, "JPEG")
