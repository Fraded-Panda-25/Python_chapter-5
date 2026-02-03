# creating a list of numbers:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]





# creating a for loop to get each numbers from the numbers variable:

for number in numbers:

    # creating a if-elif-else chain to get ordinal number:
    if number == 1:
        suffix = 'st'
        print(f"{number}{suffix}")
    elif number == 2:
        suffix = 'nd'
        print(f"{number}{suffix}")
    elif number == 3:
        suffix ='rd'
        print(f"{number}{suffix}")
    else:
        suffix = 'th'
        print(f"{number}{suffix}")
    

    


