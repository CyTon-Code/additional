def run_console(stop: str = "."):
    """
        Этот блок предназначен для прямого взаимодействия с пользователем.
    """

    console = True

    while console:
        command = input()

        if command[0] == stop:
            console = False
