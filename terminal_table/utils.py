from typing import Literal, Optional, Dict, Any
# tests+
def has_nested_lists(lst: list) -> bool:
    """проверяет, есть ли вложенные списки."""
    if not isinstance(lst, list):
        raise Exception(f"Ожидался список, получено {type(lst)}")
    return any(isinstance(item, list) for item in lst)

# tests+
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

# tests+
def add_brackets_to_row(elements: list[str], separator: str = '  ', is_borders: bool = True) -> str:
    """обьединяет столбцы """
    if separator.isspace():
        return separator.join(elements)
    body_str = f' {separator} '.join(elements)
    return f'{separator} {body_str} {separator}' if is_borders else body_str