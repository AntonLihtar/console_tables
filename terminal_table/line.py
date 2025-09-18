class Line:

    def __init__(self, column_widths: list[int], style: dict[str, any]):
        if not isinstance(column_widths, list) or not all(isinstance(w, int) and w > 0 for w in column_widths):
            raise Exception(f"Неверный формат column_widths: {column_widths}. Ожидается список положительных чисел.")

        required_keys = ['separator', 'borders', 'is_v_char']
        for key in required_keys:
            if key not in style:
                raise Exception(f"Ключ '{key}' отсутствует в словаре стиля: {style}")

        self.column_widths = column_widths
        self.style = style
        self.and_sep = len(self.style['separator']) * '-'

    def get_line_of_dashes_and_plus(self):
        return '+' + '+'.join('-' * (w + 2) for w in self.column_widths) + '+'

    def get_line_of_dashes(self):
        return self.and_sep.join(x * '-' for x in self.column_widths)
