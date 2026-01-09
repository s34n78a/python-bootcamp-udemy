import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

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

    def build_deck(self):

        for suit in suits:
            for rank in ranks:
                # bikin 52 kartu
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        # random.shuffle ga return apa"

    def reset_deck(self):
        self.all_cards = []
        self.build_deck()
        self.shuffle()

    def deal_one(self):
        '''ambil kartu paling atas'''
        return self.all_cards.pop()
    
    def __str__(self):
        cards = ''
        for card in self.all_cards:
            cards += str(card) + '\n'
        return cards

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
        if type(new_cards) == type([]): # banyak kartu sekaligus
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    # harus bisa hit dari deck (deal_one) 
    def hit(self, deck: Deck):
        self.all_cards.append(deck.deal_one())

    # cek kartu as
    def check_ace(self):
        for card in self.all_cards:
            if card.rank == 'Ace':
                return True
        return False
    
    # hitung kartu as
    def count_aces(self):
        counter = 0
        for card in self.all_cards:
            if card.rank == 'Ace':
                counter += 1
        return counter

    def display_cards(self):
        print(f"{self.name}'s hand:")
        for card in self.all_cards:
            print(f'- {card}')
        print()

    # challenge: insurance, split, double down

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
    
# player vs computer (dealer)
# menang kalau dapet 21 atau deket 21 tapi gak lebih dari 21 dibanding dealer

# game setup
# bikin deck, player, dealer
new_deck = Deck()
player = Player("Player")
dealer = Player("Dealer")

# Print an opening statement
print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.\n')

# player punya chips harus cukup buat betting
while True:
    try:
        player_chips = int(input("Enter your total chips: "))
    except:
        print('Wrong Input! Please enter a valid number.\n')
    else:
        if player_chips > 0:
            break
        else:
            print('Chips must be more than 0\n')

game_on = True

while game_on:
    # reset to start condition
    new_deck.reset_deck()
    player_points = 0
    dealer_points = 0
    player.all_cards = []
    dealer.all_cards = []
    winner = ''
    bust = ''
    player_ace = 0
    dealer_ace = 0

    # betting
    print(f'You have {player_chips} chips\n')
    bet = player_chips + 1
    while True:
        try:
            bet = int(input('Amount you want to bet: '))
        except:
            print('Wrong Input! Please enter a valid number.\n')
            continue
        else:
            if bet <= 0:
                print('Bet must be more than 0\n')
            elif bet <= player_chips:
                break
            else:
                print('Bet is too large!\n')
    print()

    # deal 2 kartu ke player dan dealer
    for _ in range(2):
        player.add_cards(new_deck.deal_one())
        player_points += player.all_cards[-1].value
        if player.all_cards[-1].rank == 'Ace':
            player_ace += 1

        dealer.add_cards(new_deck.deal_one())
        dealer_points += dealer.all_cards[-1].value
        if dealer.all_cards[-1].rank == 'Ace':
            dealer_ace += 1

    playing = True
    while playing:

        if dealer_points == 21:
            playing = False
            winner = dealer.name
        elif player_points == 21:
            playing = False
            winner = player.name
        else:
            playing = True

        if playing:
            # dealer kartu 1 terbuka 1 tertutup
            print("Dealer's hand:")
            print(f'- <card hidden>')
            print(f'- {dealer.all_cards[-1]}\n')

            # player kartu 2 terbuka
            player.display_cards()

        # player turn
        # player bakal hit sampe dia mau stand atau lebih dari 21
        while True and winner == '':
            try:
                player_move = input('Do you want to hit or stand? ')
                player_move = player_move.lower()
            except:
                print('Wrong Input! Please type "hit" or "stand"!\n')
                continue
            else:
                if player_move == 'hit':
                    player.hit(new_deck)
                    player_points += player.all_cards[-1].value
                    print(f'You drew {player.all_cards[-1]}!\n')
                    if player.all_cards[-1].rank == 'Ace':
                        player_ace += 1
                    break
                elif player_move == 'stand':
                    playing = False
                    break
                else:
                    print('Wrong Input! Please type "hit" or "stand"!\n')
                    continue
        
        print()

        # kalau lebih dari 21, player bust & game over
        # cek ada kartu ace ga, kalo ada, ubah ace dari 11 ke 1
        if player_points > 21:
            if player_ace > 0:
                player_points -= 10
                player_ace -= 1
            else:
                playing = False
                winner = dealer.name
                bust = player.name

    # dealer turn
    while winner == '':
        dealer.display_cards()
        print(f'Dealer Hand Value: {dealer_points}\n')
        # dealer bakal hit kalau player kurang dari 21
        if dealer_points < player_points and dealer_points < 17:
            dealer.hit(new_deck)
            dealer_points += dealer.all_cards[-1].value
            print(f'Dealer drew {dealer.all_cards[-1]}!')
            if dealer.all_cards[-1].rank == 'Ace':
                dealer_ace += 1
        # dealer stop kalau:
        # - dealer kurang dari 21, tapi lebih dari player, dealer menang
        # - dealer lebih dari 21 dia bust, player menang
        if dealer_points == 21:
            winner = dealer.name
            break
        elif dealer_points > player_points and dealer_points < 21:
            winner = dealer.name
            break
        elif dealer_points >= 17:
            if dealer_ace > 0:
                dealer_points -= 10
                dealer_ace -= 1
            else:
                winner = player.name
                if dealer_points > 21:
                    bust = dealer.name
                break

    print()

    # liat player menang atau dealer menang, tentuin chips player
    dealer.display_cards()
    player.display_cards()

    print(f'{winner} wins!')
    if winner == dealer.name:
        player_chips -= bet
    elif winner == player.name:
        player_chips += bet

    if bust != '':
        print(f'{bust} was busted!')
    print(f'\nPlayer Hand Value: {player_points}')
    print(f'Dealer Hand Value: {dealer_points}')
    print(f'Your total chips: {player_chips}\n')

    # minta player mau main lagi apa engga
    # itung chipsnya cukup ga
    if player_chips == 0:
        game_on = False
        print('You have no more chips! Game over!\nThanks for playing!')
    else:
        while True:
            try:
                next_round = input('Do you want to continue?\n(Type Y or N): ')
            except:
                print('Wrong Input! Please type "Y" or "N"!\n')
                continue
            else:
                if next_round.capitalize() == 'N':
                    game_on = False
                    print('Thanks for playing!')
                    break
                elif next_round.capitalize() == 'Y':
                    break
                else:
                    print('Wrong Input! Please type "Y" or "N"!\n')
                    continue
    print()