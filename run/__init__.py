"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.

from additional.ANT import ANT


def run(args=None, ant: ANT = None) -> (bool or None or list or Exception):
    """
        Меня зовут юзер. Я в зависимости от указаний в объекте ANT.
        Я могу скопировать модуль link в path - если link есть и path отсутствует.
        Я могу переместить модуль link в path - если link есть и path отсутствует.
        Я могу подключить модуль как main.py из link в sys.path - если link/main.py есть и в sys.path отсутствует.
        Я могу подключить скрипт как dream.a из link в ant.path - импортировав снова run_script

        :param args: команда и список аргументов. Касается ANT.
        :return: - возвращаю результат запущенного модуля или фальшивый.
    """
    print(args)
