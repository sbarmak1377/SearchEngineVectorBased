def file_reader(path):
    file = open(path, "r", encoding="utf-8")
    lines = []
    x = file.readline()
    while x:
        x = x.replace("\n", "")
        if len(x) > 0:
            lines.append(x)
        x = file.readline()
    file.close()
    return lines