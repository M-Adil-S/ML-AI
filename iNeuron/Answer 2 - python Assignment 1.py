#Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name.

first_name = input('Please enter your first name:')
last_name = input('Please enter your last name:')
name = first_name + ' ' + last_name

print(name[::-1])
