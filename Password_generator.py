import random
import welcome_logo_2

Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print(welcome_logo_2.welcome)
Letters_input = int(input("How many letters would you like to add in your Password ?\n"))
Symbols_input = int(input("How many symbols would you like to add in your Password ?\n"))
Numbers_input = int(input("How many numbers would you like to add in your Password ?\n"))

Password_list = []

for L in range(1, Letters_input + 1):
    char = random.choice(Letters)
    Password_list += char
for S in range(1, Symbols_input + 1):
    char = random.choice(Symbols)
    Password_list += char
for N in range(1, Numbers_input + 1):
    char = random.choice(Numbers)
    Password_list += char

# print(Password_list)   This is only for developers POV
random.shuffle(Password_list)
# print(Password_list)   This is only for developers POV
Password = ""
for char in Password_list:
    Password += char
print(f"Password = {Password}")
