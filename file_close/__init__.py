"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.

from typing import IO
from additional import FileDidNotClose


def file_close(file: IO, commit: str) -> None or Exception:
    try:  # Closes the file:
        file.close()

    except:  # The file didn't close:
        print(f"error: {commit}")
        raise FileDidNotClose  # Answer: The file won't close! We
        # throw in the program: "Exception".
