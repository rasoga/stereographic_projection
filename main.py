#!/usr/bin/python
from PIL import Image, ImageDraw
import math
import numpy as np

import progressbar

from classes.cube import Cube

print("Willkommen")

mCube = Cube("hi")

testVec = np.array([4,4])
print(testVec)

print(mCube.coordinateTransformation(testVec))
