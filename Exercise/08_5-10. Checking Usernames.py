# my website's current users:
current_users = ['Pritam', 'Arav', 'Carl', 'Admin', 'Pavel']



# my website's new users:
new_users = ['Pritam', 'carl', 'virat', 'Rohit', 'Durov'] # Note: 'carl' is lowercase here

# We create a new list where every name from current_users is forced to lowercase.
current_users_lower = [user.lower() for user in current_users]




# We check the lowercase version of the new name against our lowercase list:

for new_user in new_users:
    
    if new_user.lower() in current_users_lower:
        print("Sorry, " + new_user + " is already taken. So, enter a new username(case sensitive) and create a account again.")
    else:
        print("Welcome, " + new_user + "is available.")