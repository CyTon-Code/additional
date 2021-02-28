class ANT:
    def __init__(self, console=True, arguments=True, scripts=True):
        self.home = __file__  # Папка расположения.

        self.mode_console = console  # Можно запускать интерактивную консоль?
        self.mode_arguments = arguments  # Можно читать аргументы как команду? как правило в ней запускают модуль arg ()
        self.mode_scripts = scripts  # Можно запускать скриптовые файлы типов .a .py?

        self.ant_path = []
        self.args = []

    def set_console(self, console):
        self.mode_console = console

    def set_arguments(self, arguments):
        self.mode_arguments = arguments

    def set_scripts(self, scripts):
        self.mode_scripts = scripts

    def set_home(self, home):
        self.home = home
