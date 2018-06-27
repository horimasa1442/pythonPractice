
def str2floatList(str, splitChar):
    str = str.split(splitChar)

    res = []
    for onestr in str:
        res.append(float(onestr))

    return res