# mylambdata/polos.py

# Polo Class!
# attributes / properties (NOUNS): size, color, price
# methods (VERBS): wash, fold, sell

class Polo():
    def __init__(self, size, color):
        self.size = size
        self.color = color

    @property
    def full_name():
        return {self.size} {self.color}
    @staticmethod
    def wash(self):
        print(f"WASHING THE {self.size} {self.color} POLO!")
    
    def fold(self):
        print(f"FOLDING THE {self.size} {self.color} POLO!")
    
    def sell(self):
        print(f"SELLING THE {self.size} {self.color} POLO!")
    

# TODO: initialize a small blue polo and a large yellow polo

#df = DataFrame(________)
#df.columns
#df.head()
p1 = Polo(size="Small", color="Blue")
print(p1.size, p1.color)
p1.wash()

p2 = Polo(size="Large", color="Yellow")
print(p2.sell)