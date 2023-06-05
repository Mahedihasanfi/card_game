import random
ranks=[14,13,12,11,10,9,8,7,6,5,4,3,2]
suits =['Spades','Hearts','Diamond','Clubs']

class Deck:
    def __init__(self):
        print("Creating new deal in deck!!")
        self.cards=[(x,y) for x in suits for y in ranks]
    def shuffle(self):
        print("Shuffling Deck")
        random.shuffle(self.cards)
    def split_half(self):
        return (self.cards[:26],self.cards[26:]) 

class Hand:
    def __init__(self,cards_count):
         self.cards_count=cards_count
    def __str__(self):
        return "Have {} cards".format(len(self.cards_count))
    def add(self,added_cards):
        self.cards_count.extend(added_cards)
    def remove(self):
        return self.cards_count.pop()
    
class Player:
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
    def play_card(self):
        drawn_card = self.hand.remove()
        print("{} has shown : {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card
    def remove_war_cards(self):
        war_cards=[]
        if len(self.hand.cards_count)<3:
            return self.hand.cards_count
        else:
            for z in range(3):
                war_cards.append(self.hand.cards_count.pop())
            return war_cards
    def still_has_cards(self):
        return len(self.hand.cards_count) != 0
print("Welcome to war game, Let's play")

# Creating deck and spliting
d= Deck()
d.shuffle()
cards1,cards2=d.split_half()

#Creating players
comp = Player("Computer", Hand(cards2))
name=input("Your Name: ")
you = Player(name, Hand(cards1))
total_rounds =0
war_count = 0

while you.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Let's play!")
    print("Present board status:")
    print(you.name + " has: "+str(len(you.hand.cards_count)))
    print(comp.name + " has: "+str(len(comp.hand.cards_count)))
    print("Show card to deck!")
    print("\n")

    table_cards = []
    comp_card = comp.play_card()
    you_card = you.play_card()
    table_cards.append(comp_card)
    table_cards.append(you_card)

    if comp_card[1] == you_card[1]:
        war_count += 1
        print("War happend")
        table_cards.extend(you.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        if ranks.index(comp_card[1]) > ranks.index(you_card[1]):
            comp.hand.add(table_cards)
        else:
            you.hand.add(table_cards)
    else:
        if ranks.index(comp_card[1]) > ranks.index(you_card[1]):
            comp.hand.add(table_cards)
        else:
            you.hand.add(table_cards)


def winner():
    print("Game completed!\nTotal number of rounds: "+str(total_rounds))
    print("War was " + str(war_count) +" times")
    print("Computer has cards?",str(comp.still_has_cards()))
    print(f"{name} has cards? {str(you.still_has_cards())}")
    if str(you.still_has_cards())=="True":
        print(f"{name} is the Winner!")
    else:
        print("Computer is the Winner!")
winner()
