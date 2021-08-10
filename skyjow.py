import random

class Game: 

    nbplayer = 1

    def __init__(self):
        self.deck = []
        self.player = []
        self.turn = 0
        self.initDeck()
        self.initPlayer(self.nbplayer)

    def initDeck(self):
        for j in range(1,12):
            for i in range(10):
                self.deck.append(Card(j))
        for i in range(15):
            self.deck.append(Card(0))
        for i in range(5):
            self.deck.append(Card(-2))
        for i in range(10):
            self.deck.append(Card(-1))
        random.shuffle(self.deck)

    def initPlayer(self,nb):
        for i in range(nb):
            self.player.append(Player(self.deck))

    def newturn(self):
        self.turn = self.turn + 1
        for p in self.player:
            p.turn()

class Card:

    def __init__(self,value):
        self.visible = False
        self.value = value

    def __str__(self):
        return " ["+str(self.value)+"] "

class Player:

    table = []

    def __init__(self,deck):
        for i in range(12):
            self.table.append(deck.pop())

    def turn(self):
        for i in range(3):
            print("\n")
            for j in range(4):
                print(self.table[i+j],end='')

g = Game()
print("Turn "+ str(g.turn) )
g.newturn()