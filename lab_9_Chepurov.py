#Приклад 1

def mysplit(string):
    if not string:
        return []

    words = string.split()
    return words
# Тести
# Вивід: ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
print(mysplit("To be or not to be, that is the question"))

# Вивід: ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
print(mysplit("To be or not to be,that is the question"))

# Вивід: []
print(mysplit(""))

# Вивід: ['abc', '']
print(mysplit("abc "))

# Вивід: []
print(mysplit("   "))

#Приклад 2
number_dict = {'1': ('  #', '  #', '  #', '  #', '  #'),
               '2': ('###', '  #', '###', '#  ', '###'),
               '3': ('###', '  #', '###', '  #', '###'),
               '4': ('# #', '# #', '###', '  #', '  #'),
               '5': ('###', '#  ', '###', '  #', '###'),
               '6': ('###', '#  ', '###', '# #', '###'),
               '7': ('###', '  #', '  #', '  #', '  #'),
               '8': ('###', '# #', '###', '# #', '###'),
               '9': ('###', '# #', '###', '  #', '###'),
               '0': ('###', '# #', '# #', '# #', '###')}


def display_number(num):
    if num < 0:
        print("Число має бути невід'ємним.")
        return

    num_str = str(num)

    for level in range(5):
        for symbol in num_str:
            print(number_dict[symbol][level], end=' ')
        print()


while True:
    number_input = input('Введіть ціле число (або "q" для виходу): ')

    if number_input.lower() == 'q':
        break

    try:
        number = int(number_input)
        display_number(number)
    except ValueError:
        print("Введено неправильне число.")

#Приклад 3
text = input("Enter your message: ")
cipher = ''
for char in text:
    if char.isalpha():
        code = ord(char.upper()) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)
cipher = cipher.replace(" ", "")
print("Encrypted message:", cipher)

#Приклад 4
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if char.isalpha():
        code = ord(char.upper()) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)
print("Decrypted message:", text)

#Завдання 1
def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            code = (ord(char) - base + shift) % 26 + base
            encrypted_text += chr(code)
        else:
            encrypted_text += char
    return encrypted_text

text = input("Введіть текст для шифрування: ")

while True:
    shift = input("Введіть значення зсуву (1-25): ")
    if shift.isdigit() and 1 <= int(shift) <= 25:
        shift = int(shift)
        break
    else:
        print("Некоректне значення зсуву. Спробуйте ще раз.")

encrypted_text = caesar_cipher(text, shift)
print("Закодований текст:", encrypted_text)


