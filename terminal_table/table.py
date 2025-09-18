# для замещения отсутсвующих элементов списков
from itertools import zip_longest
from typing import Literal, Optional, Dict, Any
from terminal_table.line import Line

from terminal_table.utils import has_nested_lists, get_full_elements, add_brackets_to_row

# ------------------- Пред установки стилей -------------------
STYLES: Dict[str, Dict[str, Any]] = {
    "minimal": {"borders": False, 'is_v_char': False, 'separator': '  '},
    "classic": {"borders": True, 'is_v_char': True, 'separator': '|'},
    "header_lines": {"borders": True, 'is_v_char': False, 'separator': '  '}
}

class Table:
    def __init__(
            self,
            data,
            headers: Optional[list] = None,
            style: Optional[Literal['minimal', 'classic', 'header_lines']] = None,
            numbering: bool = False  # <-- флаг нумерации
    ):

        # Проверка типа данных
        if not isinstance(data, (list, dict)):
            raise Exception(f"Неподдерживаемый тип данных: {type(data)}. Ожидается list или dict.")

        self.rows = []
        self.headers = headers or []
        self.column_widths = []
        self.numbering = numbering

        # выбор стиля
        style_name = style or 'classic'
        if style_name not in STYLES:
            raise Exception(f"Стиль '{style_name}' не найден. Доступные стили: {list(STYLES.keys())}")
        self.style: Dict[str, any] = STYLES[style_name]

        if not data:
            # Пустые данные (None, [], "", 0 и т.д.) игнорируются — создаётся пустая таблица
            pass
        elif isinstance(data, dict):
            self.headers = list(data.keys())

            values = list(data.values())

            if values:
                first, *rest = values  # распаковываем тут для гарантии запуска zip_longest - иначе не дает
                self.rows = [list(row) for row in zip_longest(first, *rest, fillvalue=None)]

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

        # нормализация строк
        self.rows = [self._normalize_row(list(row), self.headers) for row in self.rows]

        # вычисляем самую длинную строку и
        self.column_widths = [len(x) for x in self.headers]

        for row in self.rows:
            for i, el in enumerate(row):
                el_len = len(str(el))
                if el_len > self.column_widths[i]:
                    self.column_widths[i] = el_len

        # если нумерация, добавляем отдельную колонку слева
        if self.numbering:
            num_width = len(str(len(self.rows)))  # ширина столбца по количеству строк
            self.column_widths = [max(num_width, 2)] + self.column_widths  # минимум 2 для эстетики
            self.headers = ['#'] + self.headers

    # нормализатор строк
    def _normalize_row(self, row: list, headers: list[str]) -> list[str]:
        """Приводит строку к длине headers и заменяет пустые значения на 'n/a'."""

        if not isinstance(row, list):
            raise Exception(f"Ожидался список, получено {type(row)}")

        normalized = []
        for i in range(len(headers)):
            if i < len(row):
                value = row[i]
                normalized.append("n/a" if value is None or value == "" else value)
            else:
                normalized.append("n/a")
        return normalized

    # сортировка
    def sort_by(self, column: str, reverse: bool = False):
        """Сортирует таблицу только по одной колонке."""

        if column not in self.headers:
            raise Exception(f"Колонка '{column}' не найдена в таблице. Доступные колонки: {self.headers}")

        # находим индекс колонки
        col_index = self.headers.index(column)

        # если включена нумерация — смещаем индекс на -1
        if self.numbering and col_index > 0:
            col_index -= 1

        # сортируем по выбранной колонке
        self.rows.sort(key=lambda row: row[col_index], reverse=reverse)

    def __str__(self):
        # 2 варианта событий с бордюром или нет

        sep = self.style['separator']
        is_borders = self.style['borders']
        is_v_char = self.style['is_v_char']

        # формируем строки с нумерацией
        full_rows = []
        for idx, row in enumerate(self.rows, start=1):
            r = list(row)
            if self.numbering:
                r = [str(idx)] + r
            full_rows.append(get_full_elements(r, self.column_widths))

        body = [add_brackets_to_row(x, sep, is_borders) for x in full_rows]
        body = "\n".join(body)

        # заголовки
        full_headers = get_full_elements(self.headers, self.column_widths)
        header = add_brackets_to_row(full_headers, sep, is_borders)

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
    def no_test_1list_hed():
        # Вариант 1: данные — список списков
        table = Table(
            data=[
                ["Adelaide", 1295, 1158259, 600.5],
                ["Brisbane", 5905, 1857594, 1146.4]
            ],
            headers=["City name", "Area", "Population", "Annual Rainfall"],
            numbering=True)
        print(table)


    def no_test2():
        # Вариант 1: данные — список списков
        table = Table(
            data=[["Moscow", 1000000, '12'], ["Rome", 500000, '12-sds-sdsd']],
            headers=["City", "Population", 'rest'],
            style="minimal",
            numbering=True
        )
        print(table)


    def no_test3():
        # Вариант 1: данные — список списков
        table = Table(
            data=[["Moscow", 1000000, '12'], ["Rome", 500000, '12-sds-sdsd']],
            style="header_lines",
            numbering=True
        )
        print(table)


    no_test_1list_hed()
    no_test2()
    no_test3()


    def sort_t():
        table = Table(
            data=[
                ["Moscow", 1000000, 500, "blue"],
                ["Rome", 500000, 1500, "red"],
                ["Paris", 2000000, 1000]
            ],
            headers=["City", "Population", "age", "color"],
            numbering=True,
            style="classic"
        )

        print("До сортировки:")
        print(table)

        # сортировка по населению по возрастанию
        table.sort_by("Population", reverse=True)
        print("\nПосле сортировки по Population:")
        print(table)

    sort_t()
