def run_console():
    """
    Этот блок предназначен для прямого взаимодействия с пользователем.
    """
    console = True
    while console:
        command = input()

        if command[0] == ".":
            console = False
