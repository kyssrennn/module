import math

class circle:
    def __init__(sl, x, y, r):
        sl.x = x
        sl.y = y
        sl.r = r

    def area(sl):
        return math.pi*sl.r*sl.r

