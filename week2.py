points = [(1, 2), (4, 6), (7, 8), (10, 12)]
import math
def calcDistance(point1,point2):
    x1,y1 = point1
    x2,y2 = point2
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
distances = []
for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance = calcDistance(points[i],points[j])
        distances.append(distance)
print(distances)