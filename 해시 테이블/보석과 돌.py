import collections

jewels = "aA"
stones = "aAAbbbb"

stone_dict = collections.defaultdict(int)

for stone in stones:
    stone_dict[stone] += 1

result = 0
for key in stone_dict:
    if key in jewels:
        result += stone_dict[key]

print(result)

# for key, value in jewels_dict.items():
#     if key in stones:
#         result += value

