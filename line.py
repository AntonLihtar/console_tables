class Line:

    def __init__(self, column_widths: list[int]):
        self.column_widths = column_widths or []

    def __str__(self):
        cw = self.column_widths
        if cw:
            return " ".join(cw)
        return 'список пустой'

    def get_line_of_dashes_and_plus(self):
        return '+' + '+'.join('-' * w + '--' for w in self.column_widths) + '+'

    def get_line_of_dashes(self):
        return "-".join(x * '-' for x in self.column_widths)
