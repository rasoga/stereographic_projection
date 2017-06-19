from PIL import Image, ImageDraw
import numpy as np

class Cube:
  def __init__(self, img):
    self.outSize = min(img.height, img.width)
    self.image = img.crop([0, 0, self.outSize, self.outSize])
    self.pixels = self.image.load()
  
  def generateImage():
    return
    
  def coordinateTransformation(self,x):
    squish = x * ( 4.0 / self.outSize )
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
    return

  def transformToSquare(self, x):
    return (x + 1) * self.outSize / 2
  
  def getColor(self, x):
    for i in range(len(x)):
      if x[i] == 1:
        del x[i]
        break

    y,z = self.transformToSquare(x)

    return self.pixels[y,z]
