#FUNCTIONS:
def get_meters():
    is_valid = False

    while not is_valid:
        meters_str = input('Digite um valor em metros: ').replace(',','.')
        is_valid = validate_input(meters_str)

        if not is_valid:
            print('Dados inválidos, tente novamente.')

    converted_meters_str = float(meters_str)
    return converted_meters_str


def validate_input(input):
    is_valid = True

    for char in input:
        if not ((char.isnumeric() or char == '.') and input[-1] != '.'):
            #Test if the input is a valid number(int or float)
            is_valid = False
    return is_valid


def convert_m_to_km(meters):
    return meters/1000


def convert_m_to_hm(meters):
    return meters/100


def convert_m_to_dam(meters):
    return meters/10


def convert_m_to_dm(meters):
    return meters*10


def convert_m_to_cm(meters):
    return meters*100


def conver_m_to_mm(meters):
    return meters*1000


#Converting data
meters = get_meters()
kilometers = convert_m_to_km(meters)
hectometers = convert_m_to_hm(meters)
decameters = convert_m_to_dam(meters)
decimeters = convert_m_to_dm(meters)
centimeters = convert_m_to_cm(meters)
millimeters = conver_m_to_mm(meters)

#Showing result
print('A medida de {} metros corresponde à: \n'.format(meters))
print('{} km'.format(kilometers))
print('{} hm'.format(hectometers))
print('{} dam'.format(decameters))
print('{} dm'.format(decimeters))
print('{} cm'.format(centimeters))
print('{} mm'.format(millimeters))







