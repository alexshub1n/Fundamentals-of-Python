def int_func(word):
    """
    The first letter is capitalized
    :param word: str
    :return: str
    """
    up_word = word.upper()
    low_word = word.lower()
    new_word = up_word[0] + low_word[1:]
    return new_word


user_str = input('Enter words separated by space: ')
user_list = list(user_str.split(' '))
result_str = ''
i = 0
for text in user_list:
    result_str += int_func(text) + ' '
print(result_str)
