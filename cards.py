import random

class Card:
    s = ["Clubs","Diamonds","Hearts","Spades","Small","Big"]
    r = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"T",11:"J",12:"Q",13:"K",14:"A",15:"X"}
    n = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"Ten",11:"Jack",12:"Queen",13:"King",14:"Ace",15:"Joker"}
    
    def __init__(self, suit, value):
        self.suit = self.s[suit]
        self.value = value
        self.rank = self.r[value]
        self.name = self.n[value]
    
    def __str__(self):
        return self.rank + self.suit[0]
    
    def getName(self):
        return self.name + " of " + self.suit if self.value < 15 else self.suit + " " + self.name

class Deck:
    def __init__(self, size):
        self.size = size
        self.deck = self.genDeck()*size
        self.shuffle()
    
    def __str__(self):
        return str([str(x) for x in self.deck])
    
    def genDeck(self):
        lst = []
        for i in range(52):
            lst.append(Card(i%4,i//4+2))
        lst += [Card(4,15),Card(5,15)]
        return lst
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()
