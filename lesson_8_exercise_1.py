class Date:
    my_list = []

    def __init__(self, my_date):
        self.my_date = my_date
        Date.my_list = my_date.split('-')

    @classmethod
    def type_number(cls):
        list_int = []
        for i in Date.my_list:
            i = int(i)
            list_int.append(i)
        return list_int

    @staticmethod
    def valid_number():
        new_list = Date.type_number()
        if (new_list[0] <= 31 and new_list[1] = 1) or
            (new_list[0] <= 28 and new_list[1] = 2) or
            (new_list[0] <= 31 and new_list[1] = 3) or
            (new_list[0] <= 30 and new_list[1] = 4) or
            (new_list[0] <= 31 and new_list[1] = 5) or
            (new_list[0] <= 30 and new_list[1] = 6) or
            (new_list[0] <= 31 and new_list[1] = 7) or
            (new_list[0] <= 31 and new_list[1] = 8) or
            (new_list[0] <= 30 and new_list[1] = 9) or
            (new_list[0] <= 31 and new_list[1] = 10) or
            (new_list[0] <= 30 and new_list[1] = 11) or
            (new_list[0] <= 31 and new_list[1] = 12)
            return 'Дата существует!'
        else:
            return 'Дата не существует!'





new_date = Date('04-04-1993')
print(Date.type_number())
print(Date.valid_number())
