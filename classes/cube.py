from PIL import Image, ImageDraw
import numpy as np

class Cube:
  def __init__(self, img):
    self.outSize = min(img.height, img.width)
    self.image = img.crop([0, 0, self.outSize, self.outSize])
    self.pixels = self.image.load()

  def generateImage(self, height):
    return

  def coordinateTransformation(self, x):
    return

  def getPtonSphere(self, x):
    return

  def getCubeCoordinate(slef, x):
    return

  def transfromToSquare(self, x):
    return (x + 1) * self.outSize / 2
  
  def getColor(self, x):
    for i in range(len(x)):
      if x[i] == 1:
        del x[i]
        break

    y,z = self.transformToSquare(x)

    return self.pixels[y,z]
