#Перше завдання
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#Друге завдання
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    month_lengths = [31, 28 + is_year_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_lengths[month - 1]

test_years = [1900, 2000, 2016, 1987, 2020]
test_months = [2, 2, 1, 11, 2]
test_results = [28, 29, 31, 30, 29]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

#Третє завдання
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31

def day_of_year(year, month, day):
    if not is_year_leap(year) and month == 2 and day > 28:
        return None
    elif month not in range(1, 13):
        return None
    elif day not in range(1, days_in_month(year, month) + 1):
        return None
    else:
        days = 0
        for m in range(1, month):
            days += days_in_month(year, m)
        days += day
        return days

# testing the function
test_years = [1900, 2000, 2016, 1987, 2024, 2021]
test_months = [2, 2, 1, 11, 2, 13]
test_days = [28, 29, 31, 30, 29, 31]
test_results = [31 + 28, 31 + 29, 31, 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29, None, None]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    dy = test_days[i]
    print(f'{yr}-{mo}-{dy} -> {day_of_year(yr, mo, dy)} Expected: {test_results[i]}')

#Четверте завдання
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#П'яте завдання
def liters_100km_to_miles_gallon(liters):
    miles = 100 / (liters / 3.785411784 * 1.609344)
    return miles

def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784 / (miles / 1.609344 * 100)
    return liters
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

#Шосте завдання
def is_a_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)
print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 2, 3))
print(is_a_triangle(5, 9, 3))

#Сьоме завдання
def is_a_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False

    sides = [a, b, c]
    sides.sort()

    return (sides[0] ** 2 + sides[1] ** 2) == sides[2] ** 2
