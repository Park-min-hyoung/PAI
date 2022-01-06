#973

points = [[1,3],[-2,2]]
k = 1

point_calc = []
for i, distance in enumerate(points):
    point_calc.append([distance[0] ** 2 + distance[1] ** 2, i])
point_calc.sort()

result = []
for i in range(k):
    result.append(points[point_calc[i][1]])

print(result)