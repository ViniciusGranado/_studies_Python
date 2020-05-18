def increase_n_percent(value=0, n=0):
    """
    -> Returns the given 'value' with added 'n' percent.
    :param value: Type: num. The given number to be calculated.
    :param n: Type: num. The added percentage.
    :return: 'value' with added 'n' percent.
    """
    return value + (value*n/100)


def decrease_n_percent(value=0, n=0):
    """
    -> Returns the given 'value' with subtracted 'n' percent.
    :param value: Type: num. The given number to be calculated.
    :param n: Type: num. The subtracted percentage.
    :return: Type: num. 'value' with subtracted 'n' percent.
    """
    return value - (value*n/100)


def double(value=0):
    """
    -> Returns the double of the given 'value'.
    :param value: Type: num. The given number to be calculated.
    :return: Type: num. Double of 'value'.
    """
    return value * 2


def half(value=0):
    """
    -> Returns half of the given 'value'.
    :param value: Type: num. The given number to be calculated.
    :return: Type: num. Half og the given 'value'.
    """
    return value / 2


def format_currency(value, currency='R$'):
    """
    -> Returns a given 'value' as a monetary formatted string.
    :param value: Type: num. The value to be formatted.
    :param currency: Type: str. The currency to be used in formatting.
           default = R$
    :return: Type: str. The formatted value.
    """
    return f'{currency}{value:.2f}'.replace('.', ',')
