"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


class FileDidNotClose(Exception):  # The file didn't close
    def __init__(self):
        pass
