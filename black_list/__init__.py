"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.

ERROR = ("", "-", "--", " ")  # терминал не может иметь таких аргументов или
# команд.
NEW_LINE = ("'", "\\", "'", '`')  # требуют перехода с режима консольная строка
# в режим консольное поле.
CLEAR_SPACE = (" ", "")  # массив для удаления по пробелам. первый также
# сепаратор.
CLEAR_TOP = ("", "\n", " ", ".")  # думаю это top массив, элементы которого не
# желанны в массивах.
