def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        max_area =max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

height = [int(x) for x in input("Enter the height of the lines seperated by space: ").split()]
result = max_area(height)
print("the maximum area that can be contained is:",result)


