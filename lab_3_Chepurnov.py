#Друге завдання
john = 3
mary = 5
adam = 6

print(john, ",", mary, ",", adam, "\n")

totalApple = john + mary + adam
print(totalApple, "\n")

print("Загальна кількість яблук:", totalApple)

#Третє завдання
kilometers = 12.25
miles = 7.38

print(miles, "miles is", round(miles * 1.61, 2), "kilometers", "\n")
print(kilometers, "kilometers is", round(kilometers / 1.61, 2), "miles", "\n")

#Четверте завдання
x = float(input("Введіть х: "))
y = 3 * x ** 3 - 2 * x ** 2 + 3 ** x - 1
print(y)

#П'яте завдання
#this program computes the number of seconds in a given number of hours

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
print("Goodbye")
#this is the end of the program that computes the number of seconds in 3 hour

#Шосте завдання
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))

print("Результат додавання двох чисел дорівнює = ", a + b)
print("Результат віднімання двох чисел дорівнює =", a - b)
print("Результат множення двох чисел дорівнює =", a * b)
print("Результат ділення двох чисел дорівнює =", a / b)

print("\nThat's all, folks!")

#Сьоме завдання
x = float(input("Введіть значення x:"))

a = x + 1 / x
a = x + 1 / a
a = x + 1 / a
a = x + 1 / a
y = 1 / a

print("y =", y,"\n")

#Восьме завдання
h = int(input("Початковий час (години): "))
m = int(input("Початковий час (хвилини): "))
d = int(input("Тривалість події (хвилини): "))

total_min = h * 60 + m + d
new_hour, new_min = divmod(total_min, 60)
new_hour %= 24

print(f"Кінцевий час: {new_hour:02d}:{new_min:02d}")