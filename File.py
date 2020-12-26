def file_reader(path):
    file = open(path, "r", encoding="utf-8")
    lines = []
    line = file.readline()
    while line:
        lines.append(line)
        line = file.readline()
    return lines