# Functions
def grades(*grades_tuple, sit=False):
    """
    -> Receives several grades. Return a dictionary containing the highest and
       lowest grades, the grades average, and, if sit=True, the class situation.
    :param grades_tuple: A tuple containing the grades passed to the function
                         as parameters.
    :param sit: Determine whether or not the class situation will be included
                on the return dictionary. Default = False
    :return: The dictionary containing the data.
    """
    dict_return = dict()
    dict_return['total'] = len(grades_tuple)
    dict_return['maior'] = max(grades_tuple)
    dict_return['menor'] = min(grades_tuple)
    dict_return['média'] = sum(grades_tuple) / len(grades_tuple)

    if sit:
        if dict_return['média'] < 5:
            dict_return['situação'] = 'Abaixo da média'
        elif dict_return['média'] < 7:
            dict_return['situação'] = 'Dentro da média'
        else:
            dict_return['situação'] = 'Acima da média'

    return dict_return


# Main program
class_data = grades(1, 8, 8, 4, 4, 3, 8, sit=True)
print(class_data)
