#Перше завдання
a = 0
while a < 21 :
    n = int(input("Enter the number:"))
    print(n >= 100)
    a += 1

#Друге завдання
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("The first number is greater.")
else:
    print("The second number is greater.")

#Третє завдання
input_str = input("Enter the plant name: ")

if input_str == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif input_str == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", input_str + "!")

#Четверте завдання
income = float(input("Please enter your income:"))
tax = 0

if income <= 85528:
    tax = income * 0.18 - 556.2
else:
    tax = 14839.2 + 0.32 * (income - 85528)

tax = max(0, tax)
tax = round(tax)
print("The tax is:", tax, "talers")

#П'яте завдання
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period.")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")

#Шосте завдання
secret_number = 1

print('''
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
+================================+
''')

while True:
    guess = int(input())
    if guess == secret_number:
        print("Молодець, магле! Тепер ти вільний")
        break
    else:
        print("Ха-ха! Ви застрягли у моїй петлі!")
        print("Спробуйте ще раз, магле!")

#Сьоме завдання
import time

for a in range(1, 6):
    print(a, "Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")

#Восьме завдання
while True:
    word = input("Enter word: ")
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break

#Дев'яте завдання
user_word = input("Enter word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)

#Десяте завдання
user_word = input("Введіть слово: ")
user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)

#Одинадцяте завдання
blocks = int(input("Enter the number of blocks: "))
height = 0
layer_blocks = 1

while layer_blocks <= blocks:
    height += 1
    blocks -= layer_blocks
    layer_blocks += 1

print("The height of the pyramid:", height)

#Дванадцяте завдання
n = int(input("Enter a natural number: "))
count = 0

while n != 1:
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    count += 1

print(n)
print("Number of steps:", count)