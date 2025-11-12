import pandas as pd

setDict = {}
data = pd.read_csv("zoo.csv")
properties = data.columns[1:]

universe = set()

for item in properties:
    setDict[item] = set()

for i in range(len(data)):
    row = data.iloc[i]
    name = row[0]
    for k in range(len(properties)):
        j = k + 1
        if row[j] == 1:
            setDict[properties[k]].add(name)
        universe.add(name)
isPlaying = True

def ask(text):
    temp = input(text)
    if temp != "n" and temp != "i":
        

while isPlaying:
    pass