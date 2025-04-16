import random
from itertools import chain

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Version
# random.shuffle(letters)
# password_letters = letters[:nr_letters]
# random.shuffle(symbols)
# password_symbols = symbols[:nr_symbols]
# random.shuffle(numbers)
# password_numbers = numbers[:nr_numbers]
# print(password_letters + password_symbols + password_numbers)
# password = "".join(password_letters + password_symbols + password_numbers)
# print(f"Your Password Is: {password}")

#Hard Version
random.shuffle(letters)
password_letters = letters[:nr_letters]
random.shuffle(symbols)
password_symbols = symbols[:nr_symbols]
random.shuffle(numbers)
password_numbers = numbers[:nr_numbers]
password = list(chain(password_letters, password_symbols, password_numbers))
print(password)
random.shuffle(password)
final_password = "".join(password)
print(f"Your Password Is: {final_password}")
