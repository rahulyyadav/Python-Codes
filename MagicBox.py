def calculate_visible_numbers(x, y, z, x1, y1, z1, a):
    # Initialize the sum of numbers that Vasya sees
    visible_sum = 0

    # Check if Vasya is behind or in front of the box (relative to the Z-axis)
    if z < 0:  # Behind the box
        visible_sum += a[0]
    if z > z1:  # In front of the box
        visible_sum += a[1]

    # Check if Vasya is below or above the box (relative to the Y-axis)
    if y < 0:  # Below the box
        visible_sum += a[2]
    if y > y1:  # Above the box
        visible_sum += a[3]

    # Check if Vasya is to the left or to the right of the box (relative to the X-axis)
    if x < 0:  # To the left of the box
        visible_sum += a[4]
    if x > x1:  # To the right of the box
        visible_sum += a[5]

    return visible_sum


# Input
x, y, z = map(int, input().split())  # Vasya's coordinates
x1, y1, z1 = map(int, input().split())  # Opposite corner of the box
a = list(map(int, input().split()))  # Numbers on the box faces

# Output the result
print(calculate_visible_numbers(x, y, z, x1, y1, z1, a))
