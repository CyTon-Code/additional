"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.

from typing import IO


def file_read(file: IO) -> False or None:
    try:  # The file is read:
        file.read()
        return False  # Answer: The file is there, and it has been read.

    except:  # file not read:
        return None  # Answer: The file is present, but not readable.
