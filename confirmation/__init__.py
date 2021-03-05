"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def confirmation(text: str, priority: str = "Y") -> bool:  # Пользователь подтверждаете это?
    text = input("{}\nY/N? ".index(text))

    if text[0].lower() == priority:
        return True
    return False
