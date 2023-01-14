import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
print("Welcome to the automatic password generator")
pw_letters = int(input("How many letters would you like in your password?\n"))
pw_symbols = int(input("How many symbols would you like to have in your password?\n"))
pw_numbers = int(input("How many numbers would you like to have in your password?\n"))
password = ""

for char in range(1, pw_letters + 1):
    password += random.choice(letters)
for char in range(1, pw_symbols + 1):
    password += random.choice(symbols)
for char in range(1, pw_numbers + 1):
    password += random.choice(numbers)

print(f"Your easy password is: {password} ")

password_list = []
for char in range(1, pw_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, pw_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, pw_numbers + 1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
    print(f"your hard password is:{password}")
