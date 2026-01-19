file = open('youtube.text', 'w')

try:
    file.write('Hello, YouTube!')
finally:
    file.close()

# Alternatively, using 'with' statement for better error handling
with open('youtube.text', 'w') as file:
    file.write('Hello, YouTube!')