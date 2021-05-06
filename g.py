from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Card:
    suits = ["speeds", "hearts", "diamonds", "clubs"]
    values = [None, None,
             "2", "3", "4","5","6","7","8","9","10","Jack", "Queen", "King", "Ace"]
    
    def __init__(self,v,s):
        self.value = v
        self.suit = s
    
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    def __repr__(self):
        z = self.values[self.value] + " of " + self.suits[self.suit]
        return z
class Player:
    def __init__(self, name):
        self.wins = 0
        self.name = name

class Game:
    def __init__(self):
        name1 = input("プレーヤー１の名前")
        name2 = input("プレーヤー２の名前")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    def wins(self,winner):
        w = "このラウンドは{}が勝利しました"
        w = w.format(winner)
        print(w)
    def draw(self,p1n,p1c,p2n,p2c):
        e = "{}は{}、{}は{}を引きました"
        e = e.format(p1n, p1c, p2n, p2c)
        print(e)
    def play_Game(self):
        cards = self.deck.cards
        print("戦争ゲームスタート")
        while len(cards) >= 2:
            m = "qきーで終了、それ以外でPlay:"
            res = input(m)
            if res == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
            print("\n")
            self.Show(self.p1, self.p2)
        win = self.winner(self.p1, self.p2)
        print("ゲーム終了! {} 対 {}　で　{}の勝利です".format(self.p1.wins, self.p2.wins, win))
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け!"
    def Show(self,p1,p2):
        print("現在のポイント({} {} - {} {})".format(p1.name, p1.wins, p2.name, p2.wins))
        

p = Game()
p.play_Game()
