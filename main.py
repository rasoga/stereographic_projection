#!/usr/bin/python
from PIL import Image
from classes.cube import Cube

print("Willkommen")

mCube = Cube(Image.open("test.jpg"))

mResult = mCube.generateImage(500)

# Save file to output_name
mResult.save("final.jpg", "JPEG")
