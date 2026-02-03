# my list
cars = ['audi', 'bmw', 'toyota', 'maruti', 'tata', 'ashok']




# using if statement to print uppercase bmw. Also changing other car names to title.

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    


print(cars[0] == 'audi')



if 'tata' in cars:
    print('yes') 