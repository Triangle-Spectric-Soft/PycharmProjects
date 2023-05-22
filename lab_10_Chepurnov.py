#Приклад 1
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

text = input("Введіть текст: ")

if is_palindrome(text):
    print("Текст є паліндромом.")
else:
    print("Текст не є паліндромом.")

#Приклад 2
def is_anagram(text1, text2):
    text1 = text1.lower().replace(" ", "")
    text2 = text2.lower().replace(" ", "")

    sorted_text1 = sorted(text1)
    sorted_text2 = sorted(text2)

    return sorted_text1 == sorted_text2

text1 = input("Введіть перший текст: ")
text2 = input("Введіть другий текст: ")

if is_anagram(text1, text2):
    print("Тексти є анаграмами.")
else:
    print("Тексти не є анаграмами.")

#Приклад 3
def life_digit(date):
    date = date.replace(" ", "")

    while len(date) > 1:
        total = 0
        for digit in date:
            total += int(digit)
        date = str(total)
    return int(date)

date = input("Введіть день народження (у форматі РРРГММДД, або РРРРДДММ, або ММДДРРРР): ")
digit = life_digit(date)

print("Цифра життя для дати", date, "дорівнює", digit)

#Приклад 4
while True:
    try:
        number = int(input("Введіть ціле число: "))
        print(number / 2)
        break
    except ValueError:
        print("Введене значення не є допустимим числом. Повторіть спробу...")

#Завдання 1
def check_word_hidden(word, combination):
    word = word.lower()
    combination = combination.lower()

    index = -1
    for char in word:
        index = combination.find(char, index + 1)
        if index == -1:
            return "No"
    return "Yes"

word = input("Введіть слово: ")
combination = input("Введіть комбінацію символів: ")

result = check_word_hidden(word, combination)
print(result)

#Завдання 2
def life_digit(date):
    try:
        date = date.replace(" ", "")

        while len(date) > 1:
            total = 0
            for digit in date:
                total += int(digit)
            date = str(total)
        return int(date)
    except ValueError:
        return None

while True:
    date = input("Введіть день народження (у форматі РРРГММДД, або РРРРДДММ, або ММДДРРРР): ")
    digit = life_digit(date)

    if digit is not None:
        print("Цифра життя для дати", date, "дорівнює", digit)
        break
    else:
        print("Введена дата має некоректний формат. Повторіть спробу...")


#Завдання 3
def check_integer_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value})")
            else:
                return value
        except ValueError:
            print("Error: wrong input")

lower_limit = 1
upper_limit = 100
input_prompt = f"Введіть ціле число в діапазоні {lower_limit}..{upper_limit}: "

number = check_integer_input(input_prompt, lower_limit, upper_limit)
print("Введене число:", number)
