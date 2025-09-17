from table import add_brackets_to_row


def test_with_space_separator():
    result = add_brackets_to_row(["a", "b", "c"], " ", True)
    assert result == "a b c"


def test_with_pipe_and_borders():
    result = add_brackets_to_row(["a", "b", "c"], "|", True)
    assert result == "| a | b | c |"


def test_with_pipe_without_borders():
    result = add_brackets_to_row(["a", "b", "c"], "|", False)
    assert result == "a | b | c"


def test_with_double_colon_separator():
    result = add_brackets_to_row(["1", "22"], "::", True)
    assert result == ":: 1 :: 22 ::"


def test_with_single_element():
    result = add_brackets_to_row(["solo"], "|", True)
    assert result == "| solo |"


def test_with_empty_list():
    result = add_brackets_to_row([], "|", True)
    assert result == "|  |"
