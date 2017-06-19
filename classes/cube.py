from PIL import Image, ImageDraw
import numpy as np

class Cube:
  def __init__(self, img):
    self.outSize = min(img.height, img.width)
    self.image = img.crop(
                  [np.round(.5*img.size[0])-.5*self.outSize,
                   np.round(.5*img.size[1])-.5*self.outSize,
                   np.round(.5*img.size[0])+.5*self.outSize,
                   np.round(.5*img.size[1])+.5*self.outSize])
    self.pixels = self.image.load()
    self.image.save("crop.jpg", "JPEG")
    
  def coordinateTransformation(self,x,h):
    squish = x * ( 4.0 / h )
    return (squish + np.array([-2] * len(x)))
    
  def getPtonSphere(self,x):
    if not np.any(x): #if zero vector
      ret = np.zeros(len(x)+1)
      ret[-1] = 1
      return ret
    norm = np.linalg.norm(x)
    ret = x * np.array([( 2.0 / norm**2 ) + 1] * len(x))
    return np.concatenate((ret, [ ( ( 1.0 / norm**2 ) - 1 ) / ( ( 1.0 / norm**2 ) + 1 ) ] ))
    
  def getCubeCoordinate(self, x):
    m = max(np.abs(x))
    return np.array(x) / m

  def transformToSquare(self, x):
    return np.round((x + 1) * self.outSize / 2)
  
  def getColor(self, x):
    for i in range(len(x)):
      if np.abs(x[i]) == 1.0:
        x = np.delete(x, i)
        break

    y,z = self.transformToSquare(x)

    return self.pixels[y,z]

  def generateImage(self,nSize):
    newPic = Image.new("RGB", (nSize,nSize), "white")
    draw = ImageDraw.Draw(newPic)
    
    for x in range(0,nSize):
      for y in range(0,nSize):
        scaleDown = self.coordinateTransformation(np.array([x,y]),nSize)
        onSphere = self.getPtonSphere(scaleDown)
        onCube = self.getCubeCoordinate(onSphere)
        nColor = self.getColor(onCube)
        
        draw.point((x,y), fill = nColor)
        
    del draw
    return newPic
