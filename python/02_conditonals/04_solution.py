color = input("Provide me your fruit color:")
color_in_lower = color.lower()

if color_in_lower == "green":
    message = 'unripe'
elif color_in_lower == 'yellow':
    message = 'ripe'
elif color_in_lower == 'brown':
    message = 'overripe'
else:
    message = 'unknown color'

print("your fruit is",message)