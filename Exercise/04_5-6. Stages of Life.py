# the age of the person:
age = int(input('\nEnter the age of the person: '))




# printing if statement to verify the man's type(baby/toddler/kid/teenager/adult/elder) by age:

if age == 0:
    print('Invalid')

elif age < 0:
    print("Invalid")


elif age < 2:
    print('\nthe person is a baby.')


elif age == 2 or age < 4:
    print('\nthe person is a toddler.') 


elif age == 4 or age < 13:
    print('\nthe person is a kid.')

elif age == 13 or age < 20:
    print('\nthe person is a teenager.')


elif age == 20 or age < 65:
    print('\nthe person is an adult.')


else:
    print('\nthe person is an elder.')

