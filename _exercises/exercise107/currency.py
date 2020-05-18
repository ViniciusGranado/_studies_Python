def increase_n_percent(value, n):
    """
    -> Returns the given 'value' with added 'n' percent.
    :param value: Type: num. The given number to be calculated.
    :param n: Type: num. The added percentage.
    :return: 'value' with added 'n' percent.
    """
    return value + (value*n/100)


def decrease_n_percent(value, n):
    """
    -> Returns the given 'value' with subtracted 'n' percent.
    :param value: Type: num. The given number to be calculated.
    :param n: Type: num. The subtracted percentage.
    :return: Type: num. 'value' with subtracted 'n' percent.
    """
    return value - (value*n/100)


def double(value):
    """
    -> Returns the double of the given 'value'.
    :param value: Type: num. The given number to be calculated.
    :return: Type: num. Double of 'value'.
    """
    return value * 2


def half(value):
    """
    -> Returns half of the given 'value'.
    :param value: Type: num. The given number to be calculated.
    :return: Type: num. Half og the given 'value'.
    """
    return value / 2
