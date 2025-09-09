"""
Table — главный класс. Он:

Принимает данные в разных форматах (список списков, словарь, список)
Хранит заголовки
Знает, как себя отрисовать
Поддерживает настройки стиля
"""


class Table:
    def __init__(self, data, headers=None):
        if headers:
            self.headers = headers
        else:
            self.headers = []

        if isinstance(data, dict):
            self.rows = data.values()
            self.headers = list(data.keys())
        if isinstance(data, list):
            self.rows = data

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
        "City name": ["Adelaide", "Brisbane"],
        "Area": [1295, 5905],
        "Population": [1158259, 1857594],
        "Annual Rainfall": [600.5, 1146.4]
    })  # headers не нужны — берутся из ключей

    # Вариант 3: одна строка — просто список
    table3 = Table(data=["Alice", 30, "Engineer"], headers=["Name", "Age", "Job"])

    # Настройка стиля
    # table.set_style(borders=True, numbering=True, separator_char='-', cross_char='+')

    # Вывод
    print(table)  # или table.render()
    print('table1 ', repr(table))  # или table.render()
    print('table2 ', repr(table2))  # или table.render()
    print('table3 ', repr(table3))  # или table.render()
