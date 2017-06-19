#!/usr/bin/python
from PIL import Image, ImageDraw
import math
import numpy as np

import progressbar

from classes.cube import Cube

print("Willkommen")

mCube = Cube(Image.open("earth.jpg"))

mResult = mCube.generateImage(500)

# Save file to output_name
mResult.save("final.jpg", "JPEG")
