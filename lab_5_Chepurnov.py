#Перше завдання
hat_list = [1, 2, 3, 4, 5]
number = int(input("Введіть число, щоб замінити його в списку:"))
hat_list[int(len(hat_list) // 2)] = number

print(hat_list)

del hat_list[len(hat_list) - 1]

print(hat_list)

print(len(hat_list))

#Друге завдання
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

lst = [64, 34, 25, 12, 22, 11, 90]
print("Не відсортований список: ", lst)

sorted_lst = bubble_sort(lst)

print("Відсортований список: ", sorted_lst)

#Третє завдання
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = list(set(my_list))
print("The list with unique elements only:")
print(unique_list)

#Четверте завдання
chessboard = [['_']*8 for _ in range(8)]

chessboard[0][0] = 'R'
chessboard[0][7] = 'R'
chessboard[7][0] = 'R'
chessboard[7][7] = 'R'

for row in chessboard:
    print(row)