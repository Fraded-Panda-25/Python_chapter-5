# my list:
usernames = ['Pritam', 'Arav', 'Carl', 'Admin', 'Pavel']

# print (len(usernames))
# removing each person from the list named usernames to get an empty list:

usernames.clear() 

print(usernames)

# using if statement to find if the list is empty:

if usernames == []:
    print("We need to find some users!")

# using for loop and if-elif-else statement to print a message to every usernames:


for username in usernames:
   
    if username == 'Admin':
        print("\nHello admin, would you like to see a status report?")

    
    else:
        print(username + " thank you for logging in again")
        


