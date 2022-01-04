#56

intervals = [[1,4],[2,3]]

intervals = sorted(intervals, key=lambda x: x[0])
left = intervals[0][0]
right = intervals[0][1]
result = []

for l, r in intervals[1:]:
    if l <= right:
        if r <= right:
            continue
        right = r
    else:
        result.append([left, right])
        left = l
        right = r

result.append([left, right])
print(result)