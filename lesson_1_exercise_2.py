user_seconds = int(input('Enter time in seconds: '))
hour = user_seconds//3600
minut = (user_seconds % 3600)//60
second = (user_seconds % 60)

time = f'Time is {hour:02}:{minut:02}:{second:02}'
print(time)
