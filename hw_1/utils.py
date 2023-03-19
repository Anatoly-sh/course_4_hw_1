import csv
import pathlib

dir_path = pathlib.Path.cwd()


class Item:
    """Класс вида товара с наименованием, ценой и количеством"""
    discount_rate = 0.85  # уровень цен с учетом скидки
    items_list = []  # хранение созданных экземпляров класса
    PATH_TO_FILE_CSV = f'{dir_path}/data/items.csv'

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self) -> str:
        """возвращает название товра - это getter"""
        return self.__name

    @name.setter
    def name(self, value):
        """Контролирует длину названия товара в setter"""
        if len(value) > 10:
            raise ValueError("Длина наименования товара превышает 10 символов")
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        """
        Считывает данные из csv-файла и создает экземпляры класса, инициализируя их данными из файла,
        и отправляет на хранение добавлением в список
        """
        try:
            with open(cls.PATH_TO_FILE_CSV, 'r') as file:
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    # print(row)
                    if list(row.keys()) == ['name', 'price', 'quantity']:
                        Item.items_list.append(cls(name=row['name'], price=float(row['price']),
                                                   quantity=int(row['quantity'])))
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print(f"По адресу '{cls.PATH_TO_FILE_CSV}' файл item.csv отсутствует")
        except InstantiateCSVError:
            print("Файл item.csv повреждён")

    @staticmethod
    def is_integer(num) -> bool:
        if isinstance(num, int) or (isinstance(num, float) and num % 1 == 0):
            return True
        else:
            return False

    def calculate_total_price(self):
        """получить общую стоимость конкретного товара в магазине"""
        return self.price * self.quantity

    def apply_discount(self):
        """применить установленную скидку для конкретного товара"""
        return self.price * Item.discount_rate  # дисконтная стоимость


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """возвращает количество сим-карт"""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, val):
        """Контролирует допустимое количество сим-карт"""
        if val > 0:
            self._number_of_sim = val
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Объект 'other' не принадлежит нужному классу")


class MixinLog:
    LANGUAGE = 'EN'

    def __init__(self, *args):
        self.__language = MixinLog.LANGUAGE
        super().__init__(*args)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'
        return self.__language


class KeyBoard(MixinLog, Item):
    def __init__(self, *args):
        super().__init__(*args)


class InstantiateCSVError(Exception):
    """
    Класс-исключение, обрабатывает исключения, возникающие
    при открытии csv-файла в случае его повреждения.
    Атрибут: message (сообщение об ошибке)
    Методы: __init__, __str__- возвращает строку для печати с сообщением об ошибке
    """
    def __init__(self, *args):
        self.message = args[0] if args else "Неизвестная ошибка"

    def __str__(self):
        return self.message

if __name__ == '__main__':
    # tmp1 = Tmp()
    # 4
    # item1 = Item("Смартфон", 10000, 20)
    # item2 = Phone("iPhone14", 90_000, 15, 2)
    #
    # print(item1)
    # print(item2)
    # item2.number_of_sim = 1
    # print(item2.number_of_sim)

    # print(repr(item2))
    # item2.number_of_sim = 0

    # 5
    # print(KeyBoard.__mro__)

    # kb = KeyBoard('Dark Project KD87A', 9600, 5)
    # print(kb)
    # print(kb.price)
    # print(kb.quantity)
    # print(kb.language)
    # kb.change_lang()
    # print(kb.language)
    # print(kb.__repr__())
    # kb.language = 'CH'
    # print(kb.language)
    # 6
    Item.instantiate_from_csv()
    print(len(Item.items_list))

    for raw in Item.items_list:
        print(raw.name, raw.price, raw.quantity)




