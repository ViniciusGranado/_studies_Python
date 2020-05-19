import user_register as ur
from time import sleep

# Description: This program is an user register system. It uses a CSV file to keep user's name and data. On start,
# if the file doesn't exist, the program will create it. Using an external file, the system can record data when
# program is not running.


# Check if users file exists, if not, create one
ur.data_manager.check_user_files()

# Main program
while True:
    ur.interface.print_main_menu()
    user_option = ur.data_manager.get_menu_option()

    if user_option == 1:
        users_file = ur.data_manager.open_users_file('r')
        ur.interface.show_users_table(users_file)
        sleep(2)
    elif user_option == 2:
        users_file = ur.data_manager.open_users_file('a')
        new_user_data = ur.data_manager.get_new_user_data()
        ur.data_manager.append_data_users_file(users_file, new_user_data)
        sleep(2)
    else:
        break

print('\nFinalizando...')
sleep(2)
