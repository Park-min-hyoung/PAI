# #5
s = "babad"
middle = len(s) // 2
print(s[2:-1:-1])

idx = -1
result = [[1, s[middle]]]
while True:
    if middle + idx == -1:
        break
    # 왼쪽 조회
    print(idx)
    print('hi' + s[middle:middle + idx - 1:-1], s[middle + idx: middle + 1] +'good')
    if s[middle:middle + idx - 1:-1] == s[middle + idx: middle + 1]:
        print('hi')
        result.append([len(s[middle + idx: middle + 1]), s[middle + idx: middle + 1]])
    idx *= -1

    if len(s) == middle + idx:
        break
    # 오른쪽 조회
    print(s[middle: middle + idx + 1], s[middle + idx: middle - idx: -1])
    if s[middle: middle + idx + 1] == s[middle + idx: middle - idx: -1]:
        result.append([len(s[middle: middle + idx + 1]), s[middle: middle + idx + 1]])
        print('hi')
    idx = (idx + 1) * -1