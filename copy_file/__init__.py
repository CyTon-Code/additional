def copy_file(link):
    f = open(link, "r")
    res = f.read()
    f.close()
    return res
