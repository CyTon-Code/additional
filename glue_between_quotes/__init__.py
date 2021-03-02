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
