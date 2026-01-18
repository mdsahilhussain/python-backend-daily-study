import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

print(circle_stats(5))

result_area, result_circumference = circle_stats(5)

print('Area:', result_area, 'Circumference:', result_circumference)

# how to show only two digit after decimal