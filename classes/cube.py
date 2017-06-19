import numpy as np

class Cube:
  def __init__(self,img):
    self.image = img
    self.outSize = 10.0
  
  def generateImage():
    return
    
  def coordinateTransformation(self,x):
    squish = x * ( 4.0 / self.outSize )
    return (squish + np.array([-2] * len(x)))
    
  def getPtonSphere(x):
    if not np.any(x): #if zero vector
      ret = np.zeros(len(x)+1)
      ret[-1] = 1
      return ret
    norm = np.linalg.norm(x)
    ret = x * np.array([( 2.0 / norm**2 ) + 1] * len(x))
    return np.concatenate((ret, [ ( ( 1.0 / norm**2 ) - 1 ) / ( ( 1.0 / norm**2 ) + 1 ) ] ))
    
  def getCubeCoordinate(x):
    return
  
  def getColor(x):
    return
