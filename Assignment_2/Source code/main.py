#Jordan Higgins
#Kalyani Bholane
#Computer Science 101L 005L
#September 18, 2021
#
#
#
who = input('Who are we calculating grades for? ==> \n')
labs_grade = int(input('Enter the Labs grade? ==> \n'))
if labs_grade < 0:
    print('The lab value should have been 0 or greater. It has been changed to 0')
    labs_grade = 0
elif labs_grade > 100:
    print('The lab should have been 100 or less. It has been changed to 100.')
    labs_grade = 100
exam_grades = int(input('Enter the EXAMS grade? ==> \n'))
if exam_grades < 0:
    print('The exam value should have been 0 or greater. It has been changed to 0')
    labs_grade = 0
elif exam_grades > 100:
    print('The exam should have been 100 or less. It has been changed to 100.')
    exam_grades = 100
attendance = int(input('Enter the Attendance grade? ==> \n'))
if attendance < 0:
    print('The attendance value should have been 0 or greater. It has been changed to 0')
    attendance = 0
elif attendance > 100:
    print('The attendance should have been 100 or less. It has been changed to 100.')
    attendance = 100
weight_grade = (labs_grade*.7)+(exam_grades*.2)+(attendance*.1)

print('The weighted grade for Abe is ',weight_grade)

if weight_grade >= 90:
    grade = 'A'
elif weight_grade >= 80 and weight_grade < 90:
    grade = 'B'
elif weight_grade >= 70 and weight_grade < 80:
    grade = 'C'
elif weight_grade >= 60 and weight_grade < 70:
    grade = 'D'

else: grade = 'F'

print('Abe has a letter grade of', grade)