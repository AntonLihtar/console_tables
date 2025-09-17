class Line:

    def __init__(self, column_widths: list[int], style: dict[str, any]):
        self.column_widths = column_widths
        self.style = style
        self.and_sep = len(self.style['separator']) * '-'



    def get_line_of_dashes_and_plus(self):
        return '+' + '+'.join('-' * (w + 2) for w in self.column_widths) + '+'

    def get_line_of_dashes(self):
        return self.and_sep.join(x * '-' for x in self.column_widths)
