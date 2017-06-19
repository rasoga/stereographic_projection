#!/usr/bin/python
from PIL import Image
from classes.cube import Cube

print("Willkommen")

mCube = Cube(Image.open("test_images/cat.jpg"))

mResult = mCube.generateImage(1000)

# Save file to output_name
mResult.save("final.jpg", "JPEG")
