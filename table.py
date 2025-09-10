# для замещения отсутсвующих элементов списков
from itertools import zip_longest

"""
Table — главный класс. Он:

Принимает данные в разных форматах (список списков, словарь, список)
Хранит заголовки
Знает, как себя отрисовать
Поддерживает настройки стиля
"""


def has_nested_lists(lst: list) -> bool:
    """вспомогательный метод — проверяет, есть ли вложенные списки."""
    return any(isinstance(item, list) for item in lst)


def get_full_elements(elements: list[str | int], column_widths: list[int]) -> list[str]:
    return [str(v).center(l) for v, l in zip(elements, column_widths)]


def add_brackets_to_row(elements: list[str]) -> str:
    return f'| {" | ".join(elements)} |'


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

        full_headers = get_full_elements(self.headers, self.column_widths)
        header = add_brackets_to_row(full_headers)

        full_rows = [get_full_elements(x, self.column_widths) for x in self.rows]
        body = [add_brackets_to_row(x) for x in full_rows]
        body = "\n".join(body)

        return f"\n{border}\n{header}\n{border}\n{body}\n{border}"

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


    no_test_1list_hed()
