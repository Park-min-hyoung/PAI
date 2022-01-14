#240

import bisect

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20

for i, lst in enumerate(matrix):
    find_idx = bisect.bisect_left(lst, target)
    if find_idx < len(lst) and target == matrix[i][find_idx]:
        print(True)
        exit()

print(False)

print(list(target in row for row in matrix))