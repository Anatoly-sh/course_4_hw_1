import csv


class Item:
    """Класс вида товара с наименованием, ценой и количеством"""
    discount_rate = 0.85  # уровень цен с учетом скидки
    items_list = []  # хранение созданных экземпляров класса

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        # self.items_list.append(self)

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
        with open('items.csv', 'r', encoding='windows-1251') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                Item.items_list.append(cls(name=row['name'], price=float(row['price']), quantity=int(row['quantity'])))

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


if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)

    item1
    print(item1)
