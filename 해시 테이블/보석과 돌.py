import collections
from collections import Counter

jewels = "aA"
stones = "aAAbbbb"
result = 0

# defaultdict를 이용한 비교 생략
'''stone_dict = collections.defaultdict(int)

for stone in stones:
    stone_dict[stone] += 1

for key in jewels:
    result += stone_dict[key]

print(result)'''

# Counter로 계산 생략
'''stone = Counter(stones)

for key in jewels:
    result += stone[key]'''

# 파이썬 다운 방식
'''print(sum(s in jewels for s in stones))'''

print(result)