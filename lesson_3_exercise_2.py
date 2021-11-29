def user_data(name, surname, year_of_birth, city, email, phone_number):
    """
    User data output
    :param name: str
    :param surname: str
    :param year_of_birth: str
    :param city: str
    :param email: str
    :param phone_number: str
    :return: str
    """
    user_info = f'{name} {surname}/{year_of_birth}/{city}/{email}/{phone_number}'
    return user_info


print(user_data(name=input('Enter name: '),
                surname=input('Enter surname: '),
                year_of_birth=input('Enter the year of birth: '),
                city=input('Enter city: '),
                email=input('Enter email: '),
                phone_number=input('Enter phone number: ')
                ))
