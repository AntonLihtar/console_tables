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

        if isinstance(data, dict):
            self.headers = list(data.keys())
            values = list(data.values())
            self.rows = [values if has_nested_lists(values) else [values]]

        if isinstance(data, list):

            if has_nested_lists(data):
                self.rows = data
            else:
                self.rows = [data]

            # заголовки
            if headers:
                self.headers = headers
            else:
                # если заголовков нет - ищем самый длинный элемент из списка и по ему строим заголовки
                len_list = max(len(x) for x in data)
                print('len_list ->', len_list)
                self.headers = [f'column {x + 1}' for x in range(4)]

    def __str__(self):
        return " ".join(self.headers)

    def __repr__(self):
        return f'{self.headers} , rows = {self.rows}'


if __name__ == '__main__':
    # Вариант 1: данные — список списков
    table = Table(data=[
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4]
    ], headers=["City name", "Area", "Population", "Annual Rainfall"])

    # Вариант 2: данные — словарь
    table2 = Table(data={
        "City name2": ["Adelaide", "Brisbane"],
        "Area2": [1295, 5905],
        "Population2": [1158259, 1857594],
        "Annual Rainfall2": [600.5, 1146.4]
    })  # headers не нужны — берутся из ключей

    # Вариант 3: одна строка — просто список
    # table3 = Table(data=["Alice", 30, "Engineer"])

    # Вариант 4: данные — словарь
    table4 = Table(data=[
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4]
    ])

    # Настройка стиля
    # table.set_style(borders=True, numbering=True, separator_char='-', cross_char='+')

    # Вывод
    print(table)  # или table.render()
    print('table1 ', repr(table))  # или table.render()
    print('table2 ', repr(table2))  # или table.render()
    # print('table3 ', repr(table3))  # или table.render()
    print('table3 ', repr(table4))  # или table.render()
