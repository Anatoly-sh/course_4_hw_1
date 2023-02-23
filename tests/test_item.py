import pytest
from hw_1.utils import Item


@pytest.fixture
def item_1():
    return Item('Ручка гелевая', 150, 60)


def item_2():
    return Item('Бумага уп.', 400, 50)


def test_item(item_1):
    assert item_1.name == 'Ручка гелевая'
    assert item_1.price == 150
    assert item_1.quantity == 60


def test_kind_amount(item_1):
    item2 = Item('Бумага уп.', 400, 50)
    assert item_1.calculate_total_price() == 9000
    assert item2.apply_discount() == 340

    Item.discount_rate = 0.8
    assert int(item2.apply_discount()) == 320
    Item.items_list.append(item_1)
    Item.items_list.append(item2)
    assert len(Item.items_list) == 2
