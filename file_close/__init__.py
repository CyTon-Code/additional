from typing import IO
from additional import FileDidNotClose


def file_close(file: IO, commit: str) -> None or Exception:
    try:  # Closes the file:
        file.close()

    except:  # The file didn't close:
        print(f"error: {commit}")
        raise FileDidNotClose  # Answer: The file won't close! We
        # throw in the program: "Exception".
