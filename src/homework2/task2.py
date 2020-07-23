"""Найти самое длинное слово в введенном предложении.

    В случае если их несколько, самое левое в строке Учтите что в предложении
    есть знаки препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """

    line_str = str_.split()
    new_list = list()
    for i in range(len(line_str)):
        new_list.append(line_str[i].strip('!\@#$%^&*()-"_:;|<>,./?'))
    new_list.sort(key=len, reverse=True)
    return (new_list[0])  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(longest_word(str_))
