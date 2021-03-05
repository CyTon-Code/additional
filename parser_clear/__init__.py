"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.

from additional.black_list import ERROR


def parser_clear(string):
    array = []
    for i in string:
        if not (i in ERROR):
            array.append(i)
    return array
