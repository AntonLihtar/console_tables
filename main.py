"""
Table — главный класс. Он:

Принимает данные в разных форматах (список списков, словарь, список)
Хранит заголовки
Знает, как себя отрисовать
Поддерживает настройки стиля
"""

# для замещения отсутсвующих элементов списков
from itertools import zip_longest


def has_nested_lists(lst):
    """вспомогательный метод — проверяет, есть ли вложенные списки."""
    return any(isinstance(item, list) for item in lst)


class Table:
    def __init__(self, data, headers=None):

        self.rows = []
        self.headers = headers or []

        if isinstance(data, dict):
            self.headers = list(data.keys())

            values = list(data.values())

            if values:
                first, *rest = values  # распаковываем тут для гарантии запуска zip_longest - иначе не дает
                self.rows = list(zip_longest(first, *rest, fillvalue=None))
            else:
                self.rows = []

        if data and isinstance(data, list):

            if has_nested_lists(data):
                self.rows = data
            else:
                self.rows = [data]

            # заголовки есть
            if headers:
                self.headers = headers
            else:
                if has_nested_lists(data):
                    # если вложенные списки есть - ищем самый длинный элемент из списка и по нему строим заголовки
                    len_list = max(len(x) for x in data)
                else:
                    len_list = len(data)
                self.headers = [f'column {x + 1}' for x in range(len_list)]

    def __str__(self):
        return " ".join(self.headers)

    def __repr__(self):
        return f'{self.headers} , rows = {self.rows}'


if __name__ == '__main__':
    # todo: table.set_style(borders=True, numbering=True, separator_char='-', cross_char='+')

    def test_1list_hed():
        # Вариант 1: данные — список списков
        table1 = Table(data=[
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4]
        ], headers=["City name", "Area", "Population", "Annual Rainfall"])
        print('table1 ', repr(table1))  # или table.render()


    def test_2dict_hed():
        # Вариант 2: данные — словарь
        table2 = Table(data={
            "City name2": ["Adelaide", "Brisbane"],
            "Area2": [1295, 5905],
            "Population2": [1158259, 1857594],
            "Annual Rainfall2": [600.5, 1146.4]
        })  # headers не нужны — берутся из ключей
        print('table2 ', repr(table2))  # или table.render()


    def test_3list():
        # Вариант 3: одна строка — просто список
        table3 = Table(data=["Alice", 30, "Engineer"])
        print('table3 ', repr(table3))


    def test_4list():
        # Вариант 4: список списков
        table4 = Table(data=[
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4]
        ])
        print('table4 ', repr(table4))  # или table.render()


    # test_1list_hed()
    # test_2dict_hed()
    test_3list()
    # test_4list()
