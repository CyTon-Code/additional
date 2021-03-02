from additional.black_list import ERROR


def parser_clear(string):
    array = []
    for i in string:
        if not (i in ERROR):
            array.append(i)
    return array
