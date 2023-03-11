import pytest
from hw_1.utils import Item, Phone, MixinLog, KeyBoard


class Tmp:
    pass


@pytest.fixture
def item_1():
    return Item('Ручка гелевая', 160, 60)


@pytest.fixture
def item_2():
    return Item('Бумага уп.', 400, 50)


@pytest.fixture
def item_3():
    item3 = Item('Ручка гелевая', 160, 60)
    return item3


@pytest.fixture
def phone_1():
    phone1 = Phone("iPhone14", 90_000, 15, 2)
    return phone1


@pytest.fixture
def tmp_1():
    tmp1 = Tmp()
    return tmp1


def test_item_init(item_1):
    assert item_1.name == 'Ручка гелевая'
    assert item_1.price == 160
    assert item_1.quantity == 60


def test_item_replace(item_1):
    item_1.price = 300
    assert item_1.price == 300
    with pytest.raises(Exception):
        item_1.name = "Длина наименования товара превышает 10 символов"


def test_calculate_total_price_discount(item_1):
    assert item_1.calculate_total_price() == 9600
    assert item_1.apply_discount() == 136


def test_calculate_discount(item_1):
    Item.discount_rate = 0.8
    assert item_1.apply_discount() == 128


def test_items_list(item_1, item_2):
    Item.items_list.append(item_1)
    Item.items_list.append(item_2)
    assert len(Item.items_list) == 2
    Item.items_list.pop()
    Item.items_list.pop()


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.items_list) == 5
    assert Item.items_list[3].name == "Мышка"


def test_is_integer():
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.5) is False


def test_repr_str(item_3):
    assert item_3.__repr__() == "Item('Ручка гелевая', 160, 60)"
    assert str(item_3) == 'Ручка гелевая'


def test_repr_str_phone(phone_1):
    assert phone_1.__repr__() == "Phone('iPhone14', 90000, 15, 2)"
    assert str(phone_1) == 'iPhone14'


def test_number_of_sim(phone_1):
    phone_1.number_of_sim = 11
    assert phone_1.number_of_sim == 11


def test_add(phone_1, item_1, tmp_1):
    assert phone_1 + item_1 == 75
    with pytest.raises(TypeError):
        phone_1 + tmp_1


def test_keyboard_class():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert kb.__repr__() == "KeyBoard('Dark Project KD87A', 9600, 5)"
    assert kb.language == 'EN'
    kb.change_lang()
    assert kb.language == 'RU'
    with pytest.raises(AttributeError):
        kb.language = 'CH'

