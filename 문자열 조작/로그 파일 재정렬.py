# 937
logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
data1 = []
data2 = []
for value in logs:
    input_value = list(value.split())
    if input_value[1].isalpha():
        data1.append(input_value)
    else:
        data2.append(input_value)

data1.sort(key=lambda x: (x[1], ord(x[0][0]) + ord(x[0][1])))
data1.extend(data2)
result = []
for x in data1:
    result.append(" ".join(x))

print(result)
