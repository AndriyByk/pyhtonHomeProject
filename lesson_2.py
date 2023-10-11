# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання
from typing import Callable


def to_do() -> Callable:
    todo_list: [str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list = [*todo_list, todo]
        print(get_all())

    def get_all() -> [str]:
        return todo_list

    return add_todo


do = to_do()

do("NewTodo1")
do("NewTodo2")
do("NewTodo3")


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


def expanded_form(num: int) -> str:
    digits_of_number: [str] = []

    for index, digit in enumerate(str(num)):
        if digit != "0":
            digits_of_number.append(str(digit) + "0" * (len(str(num)) - index - 1))

    return " + ".join(digits_of_number)


print(expanded_form(42))


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def decor(func) -> Callable:
    count: int = 0

    def inner(*args, **kwargs) -> None:
        nonlocal count
        count += 1
        print("-/|\-" * 10)
        func(*args, **kwargs)
        print("-\|/-" * 10)
        print(count)

    return inner


@decor
def expanded_form_two(num: int) -> None:
    digits_of_number: [str] = []

    for index, digit in enumerate(str(num)):
        if digit != "0":
            digits_of_number.append(str(digit) + "0" * (len(str(num)) - index - 1))

    print(" + ".join(digits_of_number))


expanded_form_two(42)
expanded_form_two(56)
expanded_form_two(40506)

# 46:00
