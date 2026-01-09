import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# Classes
class Card:
    # perlu suit, rank, value

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # bikin 52 kartu
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        # random.shuffle ga return apa"

    def deal_one(self):
        '''ambil kartu paling atas'''
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # ambil kartu dari atas pake pop
    def remove_one(self):
        return self.all_cards.pop(0)
    
    # nambahin kartu dari bawah pake append
    # tapi kalau nambahin bbrp kartu pake extend biar ga nested list
    def add_cards(self, new_cards):
        if type(new_cards) == type([]): # kondisi awal
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

# game setup
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

# deck bagi 2
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')

    # cek ada yg udh menang blm
    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!')
        game_on = False
        break
    
    # start new round
    # ambil terus bandingin kartu paling atas
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    # kalau kartu sama
    at_war = True # asm at war
    # pake while krn bisa aja berkali"
    while at_war:
        # kalau kartu player1 lebih gede, kartu" jadi punya dia
        if player_one_cards[-1].value > player_two_cards[-1].value: # pake -1 krn ngambil 5 kartu baru dan kartu paling baru yg dibandingin
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        # kalau kartu player2 lebih gede, kartu" jadi punya dia
        elif player_two_cards[-1].value > player_one_cards[-1].value: 
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False
        
        else:
            print('WAR!')
            # kalau lebih dikit dari 5 kartu, dianggap kalah
            if len(player_one.all_cards) < 5: # ga harus angka 5, game lebih cepet selesai kalau makin gede 
                print('Player One unable to declare war')
                print('Player Two Wins!')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declare war')
                print('Player One Wins!')
                game_on = False
                break
                
            else:
                # ambil 5 kartu dari masing" player
                # dipake utk dibandingin siapa lebih tinggi
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

