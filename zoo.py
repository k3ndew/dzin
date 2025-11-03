import pandas as pd

class Animal:
    def __init__(self, property):
        self.properties = property
        self.match = 100
    
    def Uppdate(self, statements:dict):
        Fstatements = 0
        Tstatements = 0
        for key in statements.keys():
            if statements[key] == self.properties[key]:
                Tstatements += 1
            if