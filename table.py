# для замещения отсутсвующих элементов списков
from itertools import zip_longest
from typing import Literal, Optional, Dict, Any

from line import Line

"""
Table — главный класс. Он:

Принимает данные в разных форматах (список списков, словарь, список)
Хранит заголовки
Знает, как себя отрисовать
Поддерживает настройки стиля
"""


def has_nested_lists(lst: list) -> bool:
    """проверяет, есть ли вложенные списки."""
    return any(isinstance(item, list) for item in lst)


def get_full_elements(
        elements: list[str | int],
        column_widths: list[int],
        align: Literal["left", "right", "center"] = "left"
) -> list[str]:
    """Заполняет элементы пробелами по ширине колонки."""
    result = []
    for v, l in zip(elements, column_widths):
        text = str(v)
        if align == "right":
            result.append(text.rjust(l))
        elif align == "center":
            result.append(text.center(l))
        else:
            result.append(text.ljust(l))
    return result


def add_brackets_to_row(elements: list[str], separator: str, is_borders: bool = True) -> str:
    """обьединяет столбцы """
    if separator is None or separator.isspace():
        return separator.join(elements)
    body_str = f' {separator} '.join(elements)
    return f'{separator} {body_str} {separator}' if is_borders else body_str


# ------------------- Предустановки стилей -------------------
STYLES: Dict[str, Dict[str, Any]] = {
    "minimal": {"borders": False, 'is_v_char': False, 'separator': '  '},
    "classic": {"borders": True,  'is_v_char': True,'separator': '|'},
    "header_lines": {"borders": True, 'is_v_char': False, 'separator': '  '}
}


class Table:
    def __init__(
            self,
            data,
            headers: Optional[list] = None,
            style: Optional[Literal['minimal', 'classic', 'header_lines']] = None
    ):

        self.rows = []
        self.headers = headers or []
        self.column_widths = []

        # выбор стиля
        style_name = style or 'classic'
        self.style: Dict[str, Any] = STYLES[style_name]

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

    def set_style(self, **kwargs):
        self.style.update(kwargs)

    def __str__(self):
        # 2 варианта событий с бордюром или нет

        sep = self.style['separator']
        is_borders = self.style['borders']
        is_v_char = self.style['is_v_char']

        # формируем заголовки таблицы
        full_headers = get_full_elements(self.headers, self.column_widths)
        header = add_brackets_to_row(full_headers, sep, is_borders)

        # формируем строки таблицы
        full_rows = [get_full_elements(x, self.column_widths) for x in self.rows]
        body = [add_brackets_to_row(x, sep, is_borders) for x in full_rows]
        body = "\n".join(body)

        if not is_borders:
            return f"\n{header}\n{body}"

        line = Line(self.column_widths, self.style)
        if is_v_char:
            border = line.get_line_of_dashes_and_plus()
        else:
            border = line.get_line_of_dashes()
        return f"\n{border}\n{header}\n{border}\n{body}\n{border}"

    def __repr__(self):
        return f"Table(headers={self.headers}, rows={self.rows}, column_widths={self.column_widths})"


if __name__ == '__main__':
    # todo: table.set_style(borders=True, numbering=True, separator_char='-', cross_char='+')

    def no_test_1list_hed():
        # Вариант 1: данные — список списков
        table = Table(data=[
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4]
        ], headers=["City name", "Area", "Population", "Annual Rainfall"])
        print(table)


    def no_test2():
        # Вариант 1: данные — список списков
        table = Table(
            data=[["Moscow", 1000000, '12'], ["Rome", 500000, '12-sds-sdsd']],
            headers=["City", "Population", 'rest'],
            style="minimal"
        )
        print(table)

    def no_test3():
        # Вариант 1: данные — список списков
        table = Table(
            data=[["Moscow", 1000000, '12'], ["Rome", 500000, '12-sds-sdsd']],
            style="header_lines"
        )
        print(table)


    no_test_1list_hed()
    no_test2()
    no_test3()
