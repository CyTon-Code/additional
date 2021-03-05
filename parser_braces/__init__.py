"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def parser_braces(string, sep='"'):
    # if not sep in string:
    # return [string]
    array = []
    # string += sep
    temp_string = ""

    for i in string:
        if i == sep:
            # if not temp_string in clear:
            array.append(temp_string)
            array.append(sep)
            temp_string = ""
        else:
            temp_string += i
    # print(string, array, temp_string, sep)
    # if not temp_string in clear:
    array.append(temp_string)
    return array
# parentheses. braces
