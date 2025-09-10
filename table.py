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

                el_len = len(str(el))

                if el_len > self.column_widths[i]:
                    self.column_widths[i] = el_len

    def __str__(self):

        lines = [x * '-' + '--' for x in self.column_widths]
        border = f'+{"+".join(lines)}+'
        header = f'| {" | ".join(str(h).ljust(w) for h, w in zip(self.headers, self.column_widths))} |'
        return f"{border}\n{header}\n{border}"

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

        print(table1)
        print('table1 ', repr(table1))  # или table.render()


    no_test_1list_hed()
