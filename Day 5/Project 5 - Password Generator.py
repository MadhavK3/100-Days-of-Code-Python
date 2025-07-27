import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))




#************ Method 1 *************
# password = []
# for let in range(0,nr_letters):
#     password.append(random.choice(letters))
#
# for sym in range(0,nr_symbols):
#     password.append(random.choice(symbols))
#
# for num in range(0,nr_numbers):
#     password.append(random.choice(numbers))
#
# random.shuffle(password)
# print(f"Your Password is {"".join(password)}")           # special type of function to join as a string i.e  "".join , we can try something different
#
#




#*************  Method 2  *********************

# Use password as string and add it by concatenation

password = ""
for char in range(1,nr_letters + 1):
    password += random.choice(letters)
for sym in range(1,nr_symbols + 1):
    password += random.choice(symbols)
for num in range(1,nr_numbers + 1):
    password += random.choice(numbers)

# To Shuffle
password = list(password)
random.shuffle(password)

new_password = ""
for mix in range(0,(nr_symbols+nr_numbers+nr_letters)):
    new_password += password[mix]
print(new_password)

#


#**************  Method 3  *************

#
# for char in password:
#     new_password += char
#
# print(new_password)