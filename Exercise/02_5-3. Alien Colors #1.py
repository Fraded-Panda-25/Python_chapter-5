# The colour of the alien:
alien_colour = 'green'




# printing if-elif-else statement to verify the state of the alien:

print('\nThe alien is ')


if alien_colour == 'green':
    print('dead.')      #it will print if the alien is dead.
    print('The player has earned 5 points')
elif alien_colour == 'yellow':
    print('alive.')         #it will print if the alien is alive.
    print('Miss')
elif alien_colour == 'red':
    print('injured.')          #it will print if the alien is injured.
    print('miss')




