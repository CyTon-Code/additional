from additional.black_list import CLEAR_SPACE


def parser_space(string: str) -> list:
    sep = CLEAR_SPACE[0]  # " "
    array = []  # массив для слов, которые прошли через фильтр.
    string += sep  # немножко похоже на добавление \0, чтобы
    # последнее слово не пропустить.
    temp_string = ""  # эта переменная будет хранить временные псевдо-слова.

    for i in string:  # читаю строку:
        if i == sep:  # Если буква это разделитель:
            if not (temp_string in CLEAR_SPACE):  # а слова в черном списке нет:
                array.append(temp_string)  # то, добавить как слово в масив.

            temp_string = ""  # удалить слово.

        else:  # Если буква не есть в черном списке:
            temp_string += i  # добавить до псевдо-слова эту букву

    return array  # вернуть конечный массив слов.
