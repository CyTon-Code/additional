"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def _cut_name(link: str) -> str:  # Cut filename from link:
    name = ''
    for i in link:
        name += i
        if i in "\\/":
            name = ''
    return name


def get_name_from_link(link: str) -> str or None:
    """
        I am processing file addresses and returning the filename.
        Using delimiters: / \\
    """

    # If this is not a link, but garbage, then exit:
    if link == "" or link == " " or (
            link == "\n" or link == "\t"):
        return None

    # If it is not a link, then this is the filename:
    if "/" not in link and "\\" not in link:
        return link

    # Cut filename from link:
    name = _cut_name(link)

    # Return filename:
    return get_name_from_link(name)  # reprocessing...
