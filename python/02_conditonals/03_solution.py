score = input("Provide me a score:")
score_in_int = int(score)

# for break condition or loop we use break or exit()
if score_in_int >= 90:
    grade = 'A'
elif score_in_int >=80:
    grade = 'B'
elif score_in_int >=70:
    grade = 'C'
elif score_in_int >=60:
    grade = 'D'
else:
    grade ='F'

print("Your grade is",grade)