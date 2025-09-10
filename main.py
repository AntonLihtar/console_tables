# для замещения отсутсвующих элементов списков
from itertools import zip_longest

"""
Table — главный класс. Он:

Принимает данные в разных форматах (список списков, словарь, список)
Хранит заголовки
Знает, как себя отрисовать
Поддерживает настройки стиля
"""


def has_nested_lists(lst):
    """вспомогательный метод — проверяет, есть ли вложенные списки."""
    return any(isinstance(item, list) for item in lst)


class Table:
    def __init__(self, data, headers=None):

        self.rows = []
        self.headers = headers or []
        self.column_widths = []

        if not data:
            # Пустые данные (None, [], "", 0 и т.д.) игнорируются — создаётся пустая таблица
            pass
        elif isinstance(data, dict):
            self.headers = list(data.keys())

            values = list(data.values())

            if values:
                first, *rest = values  # распаковываем тут для гарантии запуска zip_longest - иначе не дает
                self.rows = list(zip_longest(first, *rest, fillvalue=None))

        elif isinstance(data, list):

            if has_nested_lists(data):
                self.rows = data
            else:
                self.rows = [data]

            # заголовков нет
            if not headers:
                if has_nested_lists(data):
                    # если вложенные списки есть - ищем самый длинный элемент из списка и по нему строим заголовки
                    len_list = max(len(x) for x in data)
                else:
                    len_list = len(data)

                self.headers = [f'column {x + 1}' for x in range(len_list)]

        # вычисляем самую длинную строку и
        self.column_widths = [len(x) for x in self.headers]
        for row in self.rows:
            for i, el in enumerate(row):
                if len(str(el)) > self.column_widths[i]:
                    self.column_widths[i] = el

    def __str__(self):
        return " ".join(self.headers)

    def __repr__(self):
        return f"Table(headers={self.headers}, rows={self.rows}, column_widths={self.column_widths})"


if __name__ == '__main__':
    # todo: table.set_style(borders=True, numbering=True, separator_char='-', cross_char='+')

    def no_test_1list_hed():
        # Вариант 1: данные — список списков
        table1 = Table(data=[
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4]
        ], headers=["City name", "Area", "Population", "Annual Rainfall"])
        print('table1 ', repr(table1))  # или table.render()


    def no_test_2dict_hed():
        # Вариант 2: данные — словарь
        table2 = Table(data={
            "City name2": ["Adelaide", "Brisbane"],
            "Area2": [1295, 5905],
            "Population2": [1158259, 1857594],
            "Annual Rainfall2": [600.5, 1146.4]
        })  # headers не нужны — берутся из ключей
        print('table2 ', repr(table2))  # или table.render()


    def no_test_3list():
        # Вариант 3: одна строка — просто список
        table3 = Table(data=["Alice", 30, "Engineer"])
        print('table3 ', repr(table3))


    def no_test_4list():
        # Вариант 4: список списков
        table4 = Table(data=[
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4]
        ])
        print('table4 ', repr(table4))  # или table.render()


    no_test_1list_hed()
    # no_test_2dict_hed()
    # no_test_3list()
    no_test_4list()
