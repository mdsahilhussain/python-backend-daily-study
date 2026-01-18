weather = input('provide me the weather today (sunny, rainy, snowy): ')
weather_in_lower = weather.lower()

if weather_in_lower == 'sunny':
    activity = 'go for a walk'
elif weather_in_lower == 'rainy':
    activity = 'read a book indoors'
elif weather_in_lower == 'snowy':
    activity = 'build a snowman'
else:
    exit('unknown weather type')

print('Today you should', activity)