# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# --------------------
# |      TASKS       |
# --------------------

# #################################################################################
# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
def get_digit(string_line):
    result = [i for i in string_line if i.isdigit()]
    return ", ".join(result)


# st = input("Введіть текст з цифрами: ")
# print(get_digit(st))


# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка

#   23, 544, 34              #вивело в консолі

def get_number(string_line: str):
    digit_array = []
    num_str = ""
    for index, s in enumerate(string_line):

        if s.isdigit():
            num_str += s
        else:
            if num_str != "":
                digit_array.append(num_str)
                num_str = ""
        if index == len(string_line) - 1:
            digit_array.append(num_str)

    return ", ".join(digit_array)


# st = input("Введіть текст з цифрами: ")
# print(get_number(st))

# #################################################################################
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
res = [letter.upper() if letter.isalpha() else letter for letter in greeting]
print(res)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

res = [i ** 2 for i in range(51) if i % 2 == 1]
print(res)


# #################################################################################
# function
#
# - створити функцію яка виводить ліст
def print_list(our_list: list):
    print(our_list)


print_list(["love", "faith", "glory", 2000])


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def choose_max(first: int, second: int, third: int):
    maxi = max(first, second, third)
    print(maxi)
    return maxi


print(choose_max(4, 6, 34))


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def return_min_print_max(*args: [int]):
    print(max(args))
    return min(args)


print(return_min_print_max(45, 65, 34))


# - створити функцію яка повертає найбільше число з ліста
def max_from_list(our_list: list[int]):
    return max(our_list)


print(max_from_list([2, 4, 6]))


# - створити функцію яка повертає найменьше число з ліста
def min_from_list(our_list: list[int]):
    return min(our_list)


print(min_from_list([2, 4, 6]))


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_list(our_list: list[int]):
    our_sum = 0
    for digit in our_list:
        our_sum += digit
    return our_sum


print(sum_list([2, 4, 6]))


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def average_list(our_list: list[int]):
    our_sum = 0
    for digit in our_list:
        our_sum += digit
    return our_sum / len(our_list)


print(average_list([2, 4, 6]))

#
# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]

list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#   - знайти мін число
print(min_from_list(list))
#   - видалити усі дублікати
our_set = set(list)
print([elem for elem in our_set])
#   - замінити кожне 4-те значення на 'X'
print(["x" if (index + 1) % 4 == 0 else elem for index, elem in enumerate(our_set)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def show_square(side: int):
    for i in range(side):
        for j in range(side):
            if i == 0 or i == side - 1:
                print("*", end="")
            else:
                if j == 0 or j == side - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        print("")


show_square(10)


# 3) вывести табличку множення за допомогою цикла while
def show_table():
    i = 1
    j = 1

    while i < 11:
        while j < 11:
            if j < 10:
                multiplication = i * j
                if multiplication < 10:
                    print(multiplication, end="   ")
                elif multiplication < 100:
                    print(multiplication, end="  ")
                else:
                    print(multiplication, end=" ")
                j += 1
            else:
                print(i * j)
                j += 1
        j = 1
        i += 1
        print("")


show_table()

# 4) переробити це завдання під меню
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


def decorator(func):
    print("==================")
    print("Результат:")
    print(func)
    print("==================")


while True:
    print(list)
    print("1. знайти мін число\n2. видалити усі дублікати\n3. замінити кожне 4-те значення на 'X'\n4. вихід")
    select = input("Зробіть вибір: ")

    if select == "1":
        decorator(min_from_list(list))
    elif select == "2":
        our_set = set(list)
        decorator([elem for elem in our_set])
    elif select == "3":
        decorator(["x" if (index + 1) % 4 == 0 else elem for index, elem in enumerate(our_set)])
    elif select == "4":
        break
    else:
        print("Помилка! Некоректний вибір")
