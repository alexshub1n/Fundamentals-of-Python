from itertools import count, cycle

user_number = int(input('Enter start number: '))

for i in count(user_number):
    if i == 20:
        break
    else:
        print(i)

q = 0
for i in cycle(range(1, user_number + 1)):
    if q >= 20:
        break
    else:
        q += 1
        print(i)
