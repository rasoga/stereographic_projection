import unittest
import random
from PIL import Image
import numpy as np

from ..classes.cube import Cube


class TestCube(unittest.TestCase):

    def setUp(self):
        self.cube = Cube(Image.open("stereographic_projection/test.jpg"))
        self.h = random.randrange(0, 10000)
        self.x = random.randrange(0, self.h)
        n = random.randint(1, 10)
        v = []
        for i in range(n):
            v.append(random.randrange(-10000, 10000))
        self.v = np.array(v)
        self.y = random.randrange(-1, 1)

    def test_coordinateTransformation(self):
        y = self.cube.coordinateTransformation(self.x, self.h)
        self.assertGreater(y, -2)
        self.assertLess(y, 2)

    def test_getPtonSphere(self):
        y = self.cube.getPtonSphere(self.v)
        norm = np.linalg.norm(y)
        self.assertAlmostEqual(norm, 1.0)

    def test_getCubeCoordinate(self):
        y = self.cube.getCubeCoordinate(self.v)
        m = max(np.abs(y))
        self.assertAlmostEqual(m, 1.0)

    def test_transformToSquare(self):
        y = self.cube.transformToSquare(self.y)
        self.assertGreater(y, 0)
        self.assertLess(y, self.cube.outSize)


if __name__ == '__main__':
    unittest.main()
