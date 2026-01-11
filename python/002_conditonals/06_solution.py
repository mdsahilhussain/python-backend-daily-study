distance = input("Provide me the distance in km:")
distance_in_float = float(distance)

if distance_in_float > 15:
    mode = 'car'
elif distance_in_float > 3:
    mode ='bike'
else:
    mode = 'walk'

print("You should go by",mode)