from collections import defaultdict

class Bag:
    def __init__(self):
        self.bag = defaultdict(int)
        self.total = 0
    
    def add(self, key):
        self.bag[key] += 1
    
    def sum(self):
        for value in self.bag.values():
            self.total += value

    def length(self):
        return self.total

    def updateItemStats(self):
        for key, value in self.bag.items():
            self.bag[key] = value/self.total
    
    def getStats(self):
        return self.bag
