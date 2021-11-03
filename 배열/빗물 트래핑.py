#42

height = [4,2,0,3,2,5]
left, right = 0, len(height) - 1
max_left, max_right = height[left], height[right]

result = 0
while left < right:
    max_left, max_right = max(height[left], max_left), max(height[right], max_right)
    if max_left <= max_right:
        result += max_left - height[left]
        left += 1
    else:
        result += max_right - height[right]
        right -= 1

print(result)