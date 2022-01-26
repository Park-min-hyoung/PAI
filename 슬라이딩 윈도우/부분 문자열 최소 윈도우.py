#76
from collections import defaultdict

s = "aa"
t = "aa"

slide_dict = defaultdict(int)
result = []
for idx, ch in enumerate(s):
    if ch in t:
        slide_dict[ch] = idx
        if len(slide_dict) == len(t):
            idx_list = slide_dict.values()
            result.append(s[min(idx_list):max(idx_list) + 1])

print(result)
print(min(result, key=len))