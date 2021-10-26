ch = input()

data = []
for target in ch.lower():
    if target.isalnum():
        data.append(target)

if data == data[::-1]:
    print('true')
else:
    print('false')