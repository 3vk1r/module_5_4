class House:

    houses_history = []
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        if args:
            cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors
    def __str__(self):
        return f'Название {self.name}, количество этажей {self.numbers_of_floors}'
    def __len__(self):
        return self.numbers_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors < other.numbers_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors <= other.numbers_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors != other.numbers_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.numbers_of_floors + value)
        return self.numbers_of_floors

    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.numbers_of_floors + value)
        return self.numbers_of_floors

    def __iadd__(self, value):
        if isinstance(value, int):
            return House(self.name, self.numbers_of_floors + value)
        return self.numbers_of_floors

    def __del__(self):
        print(f'{self.name} снесен, но он останеться в истории')


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.numbers_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor):
                print(i)
            print(f'Вы приехали на {new_floor} этаж')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)