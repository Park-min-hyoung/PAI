#20

s = ")["
stack = [s[0]]
ch_dict = {'(': 1, ')': 2, '[': 4, ']': 5, '{': 7, '}': 8}

for ch in s[1:]:
    stack.append(ch)
    if len(stack) > 1 and ch_dict[stack[-1]] - ch_dict[stack[-2]] == 1:
        stack.pop()
        stack.pop()

print(not len(stack))