class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


my_position = Position(name='Alex', surname='Shubin', position='Analyst', wage=100000, bonus=20000)

print(my_position.name)
print(my_position.surname)
print(my_position.position)
print(my_position._income)

print(my_position.get_full_name())
print(my_position.get_total_income())
