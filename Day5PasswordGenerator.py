import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password? \n"))
n_symbols = int(input("How many symbols would you like? \n"))
n_numbers = int(input("How many numbers would you like? \n"))

password = ""
#input letters to pull letters
for char in range(1, n_letters + 1):
    password += random.choice(letters)
#input symbols to pull from symbols
for char in range(1, n_symbols + 1):
    password += random.choice(symbols)
#input numbers from numbers
for char in range(1, n_numbers + 1):
    password += random.choice(numbers)
#shuffle to output a stronger password
complex_password = list(password)
random.shuffle(complex_password)
newpassword = ''.join(complex_password)

print(f"Here is your password: {newpassword}")
