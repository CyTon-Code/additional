"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


class ANT:
    def __init__(self, console: bool = True, arguments: bool = True,
                 scripts: bool = True):
        self.home = __file__  # Папка расположения.

        self.mode_console = console  # Можно запускать интерактивную консоль?
        self.mode_arguments = arguments  # Можно читать аргументы как команду?
        # как правило в ней запускают модуль arg ()
        self.mode_scripts = scripts  # Можно запускать скриптовые файлы типов:
        # .a .py?

        self.path = []  # ссылки на скрипты. Как правило одноразовые.
        # Используются обычно при старте.
        self.args = []  # аргументы которые ANT получает при запуске.

        self.echo = ""  # @ECHO -set

    def set_console(self, console):
        self.mode_console = console

    def set_arguments(self, arguments):
        self.mode_arguments = arguments

    def set_scripts(self, scripts):
        self.mode_scripts = scripts

    def set_home(self, home):
        self.home = home
