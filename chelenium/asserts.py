def assert_false(expression, message=None):
    """Fail if expression is True"""
    if expression:
        message = f"{expression} is not False"
        raise AssertionError(message)


def assert_true(expression, message=None):
    """Fail if expression is False"""
    if not expression:
        message = f"{expression} is not True"
        raise AssertionError(message)


def assert_equal(first, second, message=None):
    """Fail if first is not equal to second. Determined by == operator."""
    if not first == second:
        message = f"{first} =/= {second}"
        raise AssertionError(message)


def assert_not_equal(first, second, message=None):
    """Fail if first is equal to second. Determined by == operator."""
    if first == second:
        message = f"{first} == {second}"
        raise AssertionError(message)