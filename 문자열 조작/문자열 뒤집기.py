#344
s = ["h","e","l","l","o"]

# reverse() 메소드를 이용한 풀이
ch.reverse()

print(ch)

# 투 포인터를 이용한 풀이
'''left, right = 0, len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

print(s)'''

