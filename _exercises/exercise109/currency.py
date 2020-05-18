def increase10percent(value=0, n=0, currency=True):
    """
    -> Returns the given 'value' with added 'n' percent.
    :param value: Type: num. The given number to be calculated.
    :param n: Type: num. The added percentage.
    :param currency: Type: bool. Indicate if the returned value will be
           formatted by the function format_currency(). Default=True
    :return: 'value' with added 'n' percent.
    """
    if currency:
        return format_currency(value + (value*n/100))

    return value + (value*n/100)


def decrease10percent(value=0, n=0, currency=True):
    """
    -> Returns the given 'value' with subtracted 'n' percent.
    :param value: Type: num. The given number to be calculated.
    :param n: Type: num. The subtracted percentage.
    :param currency: Type: bool. Indicate if the returned value will be
           formatted by the function format_currency(). Default=True
    :return: Type: num. 'value' with subtracted 'n' percent.
    """
    if currency:
        return format_currency(value - (value*n/100))

    return value - (value*n/100)


def double(value=0, currency=True):
    """
    -> Returns the double of the given 'value'.
    :param value: Type: num. The given number to be calculated.
    :param currency: Type: bool. Indicate if the returned value will be
           formatted by the function format_currency(). Default=True
    :return: Type: num. Double of 'value'.
    """
    if currency:
        return format_currency(value * 2)

    return value * 2


def half(value=0, currency=True):
    """
    -> Returns half of the given 'value'.
    :param value: Type: num. The given number to be calculated.
    :param currency: Type: bool. Indicate if the returned value will be
           formatted by the function format_currency(). Default=True
    :return: Type: num. Half og the given 'value'.
    """
    if currency:
        return format_currency(value / 2)

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
