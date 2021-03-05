"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def glue_between_quotes(rmp, cal='"', sep=" "):
    tmp = []
    text = ""
    flag = False
    blag = None
    # TODO: Нужно как-то между кавычек строки склеивать пробелами

    for i in rmp:
        if i == cal:
            flag = not flag
            # if flag:
            # i = " "
            # else:
            # i = ""

        text += i
        if flag:
            # text += i
            # if blag:
            # text += sep
            # print(1, flag, blag, text, tmp, rmp, cal)
            pass
        else:
            tmp.append(text.replace('"', ""))
            text = ""
        blag = flag
    # print(1, flag, blag, text, tmp, rmp, cal)

    print(tmp)
