strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
strs.sort()
count_strs = []

for i, word in enumerate(strs):
    count_strs.append(''.join(sorted(word)))

check = [0] * len(strs)
result = []
while True:
    target_word = count_strs[0]
    array = []
    for i in range(len(strs)):
        if not check[i]:
            target_word = count_strs[i]
            break

    for i in range(len(strs)):
        if target_word == count_strs[i]:
            array.append(strs[i])
            check[i] = 1

    result.append(array)

    if sum(check) >= len(strs):
        break

print(result)