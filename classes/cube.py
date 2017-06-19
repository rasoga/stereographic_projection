from PIL import Image, ImageDraw
import numpy as np
import progressbar

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
    self.bar = progressbar.ProgressBar()


  def coordinateTransformation(self, x, h):
    squish = x * 4.0 / h 
    return squish - 2

  def getPtonSphere(self, x):
    norm = np.linalg.norm(x)
    ret = x * 2.0 / (norm**2 + 1)
    return np.append(ret, (norm**2 - 1) / (norm**2 + 1))

  def getCubeCoordinate(self, x):
    m = max(np.abs(x))
    return np.array(x) / m

  def transformToSquare(self, x):
    res = np.floor((x + 1) * self.outSize / 2)
    res[res >= self.outSize] = self.outSize - 1

    return res

  def getColor(self, x):
    for i in range(len(x)):
      if np.abs(x[i]) == 1.0:
        x = np.delete(x, i)
        break

    if len(x) != 2:
      raise Exception("Not on boundary")
    if max(np.abs(x)) > 1:
      raise Exception("Not in square")

    y,z = self.transformToSquare(x)

    return self.pixels[y,z]

  def generateImage(self, nSize):
    newPic = Image.new("RGB", (nSize, nSize), "white")
    draw = ImageDraw.Draw(newPic)

    for x in self.bar(range(nSize)):
      for y in range(nSize):
        scaleDown = self.coordinateTransformation(np.array([x,y]),nSize)
        onSphere = self.getPtonSphere(scaleDown)
        onCube = self.getCubeCoordinate(onSphere)
        nColor = self.getColor(onCube)
        draw.point((x, y), fill=nColor)

    del draw
    return newPic
