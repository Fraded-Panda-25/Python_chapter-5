# Marks of the student:

Marks = int(input('\nEnter the number of the student:'))





# using  if-elif-else statement to print the grade

print('Marks of the student ', Marks, '\ngrade of the student is:')

if Marks >= 90:
    print('\t\tgrade-A+')

elif Marks >= 80:
    print('\t\tgrade-A')

elif Marks >= 70:
    print('\t\tgrade-B')

elif Marks >= 60:
    print('\t\tgrade-C')

elif Marks >= 30:
    print('\t\tgrade-D')

else :
    print('\t\tFail')
