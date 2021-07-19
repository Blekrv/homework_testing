import pytest
import math


def kvadrat(a, b, c):

    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    if dis > 0:
        x1 = (-b + sqrt_val)/(2 * a)
        x2 = (-b - sqrt_val)/(2 * a)
        return (x1, x2)
    elif dis == 0:

        x1 = -b / (2 * a)
        return x1

    else:
        return None


class TestQuadraticEquation:

    def test1(self):
        assert kvadrat(2, 1, -1) == (0.5, -1.0)

    def test2(self):

        assert kvadrat(1, -4, 4) == 2.0

    def test3(self):

        assert kvadrat(4, 1, 2) == None
