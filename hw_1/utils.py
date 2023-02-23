import csv

class Item:
    """Класс вида товара с наименованием, ценой и количеством"""
    discount_rate = 0.85        # уровень цен с учетом скидки
    items_list = []             # хранение созданных экземпляров класса

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.items_list.append(self)

    @property
    def name(self) -> str:
        """возвращает название товра - это getter"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Контролирует длину названия товра в setter"""
        if len(value) <= 10:
            self.__name = value
        else:
            print('Exception: Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self):
        """получить общую стоимость конкретного товара в магазине"""
        return self.price * self.quantity

    def apply_discount(self):
        """применить установленную скидку для конкретного товара"""
        return self.price * Item.discount_rate  # дисконтная стоимость (проверить!)


if __name__ == '__main__':
    # item1 = Item("Смартфон", 10000, 20)
    # Item.items_list.append(item1)
    # item2 = Item("Ноутбук", 20000, 5)
    # Item.items_list.append(item2)
    #
    # print(item1.calculate_total_price())
    # print(item2.calculate_total_price())
    #
    # Item.discount_rate = 0.8  # устанавливаем новый уровень цен
    #
    # print(item1.price)
    # print(item1.apply_discount())
    # print(Item.items_list[0].name)
    # print(Item.items_list[0].price)
    # print(Item.items_list)

    @classmethod
    def instantiate_from_csv(cls, path: str) -> None:
        with open(path) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                cls(name=row[' name'],
                    price=float(row['price']),
                    quantity=int(row['quantity'])
                    )


    @staticmethod
    def is_integer(num) -> bool:
        if isinstance(num, int) or (isinstance(num, float) and num % 1 == 0):
            return True
        else:
            return False
