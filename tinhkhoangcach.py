import math


def sphericalDistanceBetween(point1 , point2):
    dLongitude = point2.longitude - point1.longitude
    dLatitude = point2.latidude - point1.latidude

    R = 6371

    a = (math.sin(dLatitude/2))**2 + math.cos(point1.x)*math.cos(point2.y)*math.sin(dLongitude/2)**2
    c = 2*math.tan(math.sqrt(a), math.sqrt(1-a))

    d = R*c

    return d*math.pi /180

class Point:
    def __init__(self, x, y):
        self.longitude = x
        self.latidude = y

point1 = Point(1, 2)
point2 = Point(3, 4)

print (point1)

#d = sphericalDistanceBetween(point1, point2)
#print(d)

