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
        return self.price * Item.discount_rate  # дисконтная стоимость (проверить!)


if __name__ == '__main__':
    # print(len(Item.items_list))
    # item1 = Item('Ручка гелевая', 150, 60)
    # item1.name = 'Суперсмартфон'
    # print((Item.items_list[0].name))
    #
    # # !!!!!!!!!!!!!!!! - это имя (адрес/ссылка) первого экземпляра: Item.items_list[1]
    # print(type(Item.items_list[0]))

    Item.instantiate_from_csv()
    print(len(Item.items_list))
    #
    # '''ожидаемое поведение'''
    # item = Item('Телефон', 10000, 5)
    # item.name = 'Смартфон'
    # print(item.name)
    #
    # item.name = 'Суперсмартфон'
    # print(item.name)
    #
    # print(Item.is_integer(5))
    # print(Item.is_integer(5.0))
    # print(Item.is_integer(5.5))

    # with open('items.csv', 'r', encoding='windows-1251') as fil:
    #     csv_fil = csv.DictReader(fil)
    #     for i in csv_fil:
    #         print(i)
    #     print(fil.read())
    # print(Item.items_list[4].name)  # из списка товаров

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

