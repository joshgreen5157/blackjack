# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import shuffle
from enum import Enum

class Card:
    def __init__(self, suit, rank, value):
        self.__suit = suit
        self.__rank = rank
        self.__value = value

        if self.__value > 10:
            self.__value = 10

    def showcard(self):
        return (self.__suit, self.__rank)

    def getvalue(self):
        if self.__value == 1:
            self.__value = 11
        return self.__value

    def getrank(self):
        return self.__rank

    def getsuit(self):
        return self.__suit

class Shoe:
    def __init__(self, decks):
        self.stack = []
        Rank = Enum('Rank', 'A 2 3 4 5 6 7 8 9 10 J Q K')
        Suit = Enum('Suit', 'Hearts Clubs Diamonds Spades')
        while decks > 0:
            for suit, member in Suit.__members__.items():
                for rank, member in Rank.__members__.items():
                    self.stack.append(Card(suit, rank, member.value))
                    decks = decks - 1
        shuffle(self.stack,)

    def get_deck(self):
        return self.stack


class BlackJack:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.game()

    def deal(self, target=None, open=False):
        if open:
            for i in range(2):
                self.dealer.hand.append(self.shoe.pop(0))
                self.player.hand.append(self.shoe.pop(0))
        else:
            target.hand.append(self.shoe.pop(0))

    def game(self):
        shoe = Shoe(3)
        self.shoe = shoe.get_deck()
        self.deal(open=True)
        self.play = True
        while self.play:
            print("Dealer shown: ")
            print(self.dealer.hand[0].showcard())
            if self.dealer.gethandvalue() == 21:
                self.play = False
            print("Player hand: ")
            self.player.showhand()
            print(self.player.gethandvalue())
            self.player_turn()
            self.dealer_turn()
            self.winner()
            self.play = False

    def player_turn(self):
        player_turn = True
        while player_turn:
            self.player.showhand()
            print(self.player.score)
            if input("Do you want to (h)it or (s)tay?") == 'h':
                self.deal(target=self.player)
                self.player.gethandvalue()
                if not self.player.brokeflag:
                    print("Broke")
                    player_turn=False
            else:
                player_turn = False

    def dealer_turn(self):
        print(self.dealer.getscore())
        while self.dealer.getscore() < 17:
            self.deal(target=self.dealer)
            self.dealer.gethandvalue()


    def winner(self):
        if self.player.gethandvalue() > self.dealer.gethandvalue() and self.player.gethandvalue() < 22:
            self.playerwins()
        else:
            self.dealerwins()
        print("Player Score:" + str(self.player.gethandvalue()))
        print("Dealer Score:" + str(self.dealer.gethandvalue()))

    def playerwins(self):
        print("Player wins this round")
        self.player.showhand()

    def dealerwins(self):
        print("Dealer wins this round")
        self.dealer.showhand()

class Player:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.brokeflag = False

    def showhand(self):
        for card in self.hand:
            print(card.showcard())

    def gethandvalue(self):
        self.score = 0
        aceflag = False
        for card in self.hand:
            if card.getrank() == 'A':
                aceflag = True
            self.score = self.score + card.getvalue()
            if self.score > 21:
                self.brokeflag = True
        if aceflag:
            while self.score > 21:
                self.score = self.score - 10
                aceflag = False

        return self.score

    def getscore(self):
        return self.score

class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.hand = []
        self.score = 0


if __name__ == '__main__':
    game = BlackJack()
