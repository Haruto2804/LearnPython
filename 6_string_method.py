name = "haruto"
phone_number = "0395-678-999"
# result = len(name) - Length of string
# result = name.find(" ") - First index of character
#result = name.rfind("q") - Last index of character
# name = name.capitalize() - Capitalize the first letter of the string
#name = name.upper() - Convert all letters to uppercase 
# name = name.lower() - Convert all letters to lowercase
# result = name.isdigit()
# result = name.isalpha() - Check if all characters are alphabetic
# result = name.isalnum() - Check if all characters are alphanumeric
# result = phone_number.count("-") - Count the number of occurrences of a character in the string
# phone_number = phone_number.replace("-", "") - Remove all occurrences of a character in the string
#phone_number)

#For more function of string
#print(help(str))

#Exercise validate user input exercise
# 1. username is no more than 12 character
# 2. username must not contain spaces
# 2. username must not contain digits
username = "haruto28 04"

if(len(username)> 12):
    print("Username can't be more 12 characters")
elif not username.find(" ") == -1:
    print("Username can't containt spaces")
elif username.isalpha():
    print("Username must not contain digits")
else:
    print(f"Welcome {username}")