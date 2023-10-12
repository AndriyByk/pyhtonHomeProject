from abc import ABC, abstractmethod


# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

class Rectangle:
    __square = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__square = x * y

    def __add__(self, other):
        return self.__square + other.__square

    def __sub__(self, other):
        return self.__square - other.__square

    def __eq__(self, other):
        return self.__square == other.__square

    def __ne__(self, other):
        return self.__square != other.__square

    def __le__(self, other):
        return self.__square <= other.__square

    def __gt__(self, other):
        return self.__square >= other.__square

    def __len__(self):
        return self.__y * 2 + self.__x * 2


rectangle1 = Rectangle(2, 6)
rectangle2 = Rectangle(5, 3)

print(rectangle1 - rectangle2)
print(rectangle1 + rectangle2)
print(rectangle1 < rectangle2)
print(rectangle1 > rectangle2)
print(rectangle1 == rectangle2)
print(rectangle1 != rectangle2)
print(len(rectangle1))
print(len(rectangle2))


###############################################################################

# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Cinderella(Human):
    def __init__(self, name: str, age: int, foot_size: int) -> None:
        super().__init__(name, age)
        self.foot_size = foot_size


class Prince(Human):

    def __init__(self, name: str, age: int, tufla_size: int) -> None:
        super().__init__(name, age)
        self.size = tufla_size

    def verify(self, cinderella_list: [Cinderella]) -> str:
        flag = False
        cinderella_name = ""
        for cinderella in cinderella_list:
            if self.size == cinderella.foot_size:
                flag = True
                cinderella_name = cinderella.name
                break
        if flag:
            return "Name of true cinderella is " + cinderella_name
        else:
            return f'Prince {self.name} did not find his cinderella :('


cinderella1 = Cinderella("Inna", 40, 38)
cinderella2 = Cinderella("Julia", 23, 37)
cinderella3 = Cinderella("Oksana", 34, 36)
cinderella4 = Cinderella("Dasha", 27, 39)

prince1 = Prince("Oleksandr", 31, 36)

print(prince1.verify([cinderella1, cinderella2, cinderella4]))
print(prince1.verify([cinderella1, cinderella2, cinderella3, cinderella4]))


###############################################################################

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()

# для перевірки ксассів використовуємо метод isinstance, приклад:
# max = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):

    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


class Magazine(Printable):

    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


class Main:
    printable_list: list[Magazine | Book] = []

    @classmethod
    def add(cls, printable):
        if isinstance(printable, Magazine) or isinstance(printable, Book):
            cls.printable_list.append(printable)

    @classmethod
    def show_all_magazines(cls):
        for printable in cls.printable_list:
            if isinstance(printable, Magazine):
                printable.print()

    @classmethod
    def show_all_books(cls):
        for printable in cls.printable_list:
            if isinstance(printable, Book):
                printable.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
