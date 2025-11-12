file = "zoo.csv"
with open(file, "r", encoding="utf-8") as f:
    header = f.readline()
    header = header.split(",")
    del(header[0])
    del(header[-1])
    print(header)