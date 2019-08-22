import random

game_instructions = """
Game Description and rules of the game:
Blackjack is a game that is played with 1 or more players and a dealer.
the objective of the game is to beat the dealer by getting
close to 21 without going over.

You can beat the dealer by:
    A. By drawing a hand value of 21 on your first two cards
    Note: it is considered a tie if the dealer's hand value is 21 within the first 2 dealer cards
    B. Drawing a hand value that is higher than the dealer’s hand value
    C. Staying under 21 when the dealer's hand value goes over 21.


Card or Point Value:
The game will be played with one deck of cards (initially).  A standard
deck of cards contains 52 cards.  Point values for the cards are:
    A. Face cards (Jack, Queen, King) = 10 pts
    B. Ace = either 1 point or 11 points depending on which value helps the hand the most.
    C. All other cards = the value on the card (ex. 2 on the card counts as 2, a 9 counts as 9)

End game payouts
    A. The dealer busts:
       The player receives 2 * Wager if the player does not go over 21 and dealer busts
    B. The player's hand is higher than the dealer:
       Similar to option A, the player receives 2 * Original bet
    C. The player's hand is equal to the dealers:
       (includes the initial blackjack scenario and if the hands are worth the same)
       The original bet is returned to the player
    D. The player's hand is lower than the dealers:
       (includes the player "busting")
       The player loses the bet
"""


# While loop to keep playing (wager)
# Overview of game
print("\n, Welcome to BlackJack!!!")
print(game_instructions)

# condition to stay in loop
game_counter = 0
while True:
    action = input("What would you like to do? Enter 'Play', 'Quit', 'Help' or 'Continue' previous game: ").lower()

    # if quit, exit program
    if action == "quit":
        print("Ending game. Thank you for playing Blackjack!")
        break

    # if help, print help instructions
    if action == "help":
        print(game_instructions)

    # if continue, use info from previous session
    if action == "continue" and game_counter > 0:
        for player in player_list:
            player.player_info()
            while True:
                try:
                    wager = int(input(player.name + ". Please enter your wager amount: "))
                except ValueError:
                    print("You did not enter a valid amount.  Please re-enter a valid amount")
                    continue
                if wager <= player.balance:
                    player.player_wager(wager)
                    break
                else:
                    print("Your wager is greater than your total balance.  Please re-enter")

        Game(player_list)
        for player in player_list:
            player.player_info()
            player.reset_values()
            if player.balance <= 0:
                print("Ending game. One or more player(s) has no remaining funds to play. Thank you for playing Blackjack!")
                quit()
            else:
                continue

    if action == "continue" and game_counter == 0:
        print("You cannot choose this option since this is your first game")

    # if play, continue addt'l steps for game
    if action == "play":
        print("Beginning Game!!!\n...\n...... \n...")


        class Player:
            """The purpose of this class is to keep track
            of the player's info"""

            def __init__(self, name, balance):
                """initializes player class and initializes attributes
                and variables"""
                self.name = name
                self.balance = balance
                self.hand = []
                self.card_total = 0
                self.card_tot = 0
                self.amount_aces = 0
                self.aces = 0

            def player_info(self):
                """method to capture info about the player"""
                print("Name: " + str(self.name))
                print("Total balance is $" + str(self.balance) + "\n")

            def return_cards(self):
                """returns card info"""
                index = 0
                return self.hand

            def add_card(self, added_cards):
                """method to add card"""
                #add cards to hand
                self.hand = self.hand + added_cards
                for added_card in added_cards:
                    # get card at positon 0
                    value = added_card.split(" ")[0]
                    # for Jack, Queen, King, return a value of 10
                    if value in ["J", "Q", "K"]:
                        value = 10
                    # for an Ace,return a value of 11 (base case)
                    elif value == "A":
                        value = 11
                        # track num of aces in hand
                        self.amount_aces += 1
                    else:
                        # convert string value into an integer
                        value = int(value)
                    self.card_total += value

                # Condition to convert Ace from 11 to 1 if needed
                if self.card_total > 21 and self.amount_aces >= 1:
                    self.card_total = self.card_total - 10
                    self.amount_aces -= 1

                def strategy(self):
                    """strategy for dealer and player"""
                    for card in self.hand:
                        # get card at positon 0
                        value = card.split(" ")[0]
                        # for Jack, Queen, King, return a value of 10
                        if value in ["J", "Q", "K"]:
                            value = 10
                        # for an Ace,return a value of 11 (base case)
                        elif value == "A":
                            value = 11
                            # track num of aces in hand
                            aces += 1
                        else:
                            # convert string value into an integer
                            value = int(value)
                        self.card_tot += value

                    # Condition to convert Ace from 11 to 1 if needed
                    if self.card_tot > 21 and aces >= 1:
                        self.card_tot = self.card_tot - 10
                        aces -= 1
                    if self.card_tot < 17:
                        return str("Hit")
                    elif self.card_tot == 21:
                        return str("Stay, you have 21!!!")
                    else:
                        return str("Stay")



            def top_card(self):
                """Method to get top Card"""
                return self.hand[0]

            def player_wager(self, wager):
                """Method to set wager"""
                self.wager = wager

            def add_wager(self):
                """Method to add wager"""
                self.balance = self.balance + self.wager

            def deduct_wager(self):
                """Method to deduct wager"""
                self.balance = self.balance - self.wager

            def reset_values(self):
                """Method to reset all initialized attributes and values"""
                self.wager = 0
                self.hand = []
                self.card_total = 0



        # Loop to ensure that a number is entered
        while True:
            try:
                num_players = int(input("How many players will be playing today?: "))
                break
            except:
                print("You did not enter a correct number of players.  Please re-enter")

        # loop to capture number of players and basic player info
        player_list = []
        for i in range(num_players):
            try:
                p1 = Player(str(input("Please enter your name: ")),
                     int(input("Enter the total amount of money($) that you would like to use during this session: ")))
                player_list.append(p1)
            except ValueError:
                print("You did not enter a valid amount.  Please re-enter name and amount")

        # loop to error proof and capture a specific wager amount
        for player in player_list:
            player.player_info()
            while True:
                try:
                    wager = int(input("Enter your wager amount for this hand: "))
                except ValueError:
                    print("You did not enter a valid amount.  Please re-enter a valid amount")
                    continue
                if wager <= player.balance:
                    player.player_wager(wager)
                    break
                else:
                    print("Your wager is greater than your total funds.  Please re-enter")


        class PlayingCard:
            """This class accepts the rank and suite attributes"""

            def __init__(self, rank, suit):
                """initialization of rank and suit"""
                self.rank = rank
                self.suit = suit

            # return output of the class in the format rank "of suit"
            def __str__(self):
                return self.rank + " of " + self.suit


        class Deck:
            """This holds the list of PlayingCard objects."""

            #setting base case for suit = None so that cards will default to the 52 cards
            def __init__(self):
                self.cards = []
                self.create()


            def create(self):
                """method to create all the combinations of the cards"""
                for r in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
                    for s in ["♠", "♥", "♦", "♣"]:
                        self.cards.append(str(PlayingCard(r, s)))

            # return output of the card list
            def __str__(self):
                return self.cards

            def shuffle_deck(self):
                # Calling the function to randomly shuffle the cards int eh deck
                # from https://docs.python.org/3.7/library/random.html
                random.shuffle(self.cards)

            def deal_card(self, card_count):
                if card_count > len(self.cards):
                    raise Exception("Cannot deal " + str(card_count) + " cards. The deck only has " + str(len(self.cards)) + " cards left!")
                else:
                    temp = self.cards[:card_count]
                    self.cards = self.cards[card_count:]
                    return temp



        class Game:
            """The purpose of this class is to keep track
            of the overall game progression (see # 3 above)"""
            def __init__(self, players):
                """Initializes the deck, deck.shuffle and players"""
                self.deck = Deck()
                self.deck.shuffle_deck()
                self.players = players

                # deals the players 2 cards
                for player in self.players:
                    player.add_card(self.deck.deal_card(2))

                print("Dealing Hand...\n")

                self.run_game() # call method run_game


            def run_game(self):
                """method to run game"""

                # dealer name and total_amount specified
                self.dealer = Player("Dealer", 0)

                # deals 2 cards to the dealer
                self.dealer.add_card(self.deck.deal_card(2))

                # keeps track of player turn (need to detemine which class this is in)
                for player in self.players:
                    self.player_turn(player)

                # strategy for the dealer.
                dealer_action = self.dealer.strategy(return_cards())

                # actions for dealer (Hit, Stay.  Dealer cannot split)
                if dealer_action == "Hit":
                    self.dealer.add_card(self.deck.deal_card(1)) # gives dealer 1 card
                if dealer_action == "Stay":
                    self.dealer.add_card(self.deck.deal_card(0)) # gives dealer 0 cards

                # determine dealer total.
                print("Dealer's cards are:" + str(self.dealer.return_cards()))
                dealer_total = self.dealer.card_total


                # Scenario/Actions if dealer is above 21
                if dealer_total > 21:
                    for player in self.players:
                        print(player.name + " has" + str(player.return_cards())) #get cards for a player
                        # Player Win Scenario: Add to wager if player is lt 21
                        if player.card_total <= 21:
                            print("You Win!!! \n")
                            player.add_wager()
                        # Player Lose Scenario: Deduct wager if player is gt than 21
                        else:
                            print("You Lose \n")
                            player.deduct_wager()

                # Scenario/Actions if dealer and player's hands  and player is less than 21
                else:
                    for player in self.players:
                        print(player.name + " has" + str(player.return_cards())) #get cards for a player

                        # Player Win Scenario: Add to wager if player is gt dealer but lt 21
                        if player.card_total > dealer_total and player.card_total <= 21:
                            print("You Win!!! \n")
                            player.add_wager()

                        # Tie scenario: do nothing if dealer & player card totals are equal
                        elif player.card_total == dealer_total:
                            print("You and the Dealer Tie.  This hand is a draw.  Your balance remains the same!!! \n")
                            continue

                        # Player lose scenario: deduct wager from player
                        else:
                            print("You Lose. \n")
                            player.deduct_wager()


            def player_turn(self, player):
                """Method for player turn"""

                # Activities to display for player
                print("It is " + player.name + "'s turn") # player's turn
                print(player.name + " has " + str(player.return_cards())+ "\n") # get cards for a player
                print("Dealer has a " + "[" + self.dealer.top_card() + "]") # get top card for dealer
                print("Recommended action: " + player.strategy(return_cards()) + "\n") # recommended action for player

                # Determine course of acton
                answer = input('What would you like to do? "Hit" or "Stay"?: ').lower()
                if answer == "hit":
                    player.add_card(self.deck.deal_card(1)) # gives each player 1 card
                    if player.card_total <= 21:
                        self.player_turn(player)


                if answer == "stay":
                    player.add_card(self.deck.deal_card(0)) # gives each player 0 card

                if answer != "hit" and answer != "stay":
                    print('You did not enter a correct value.  Please enter "Hit" or "Stay"')
                    self.player_turn(player)

        # runs game for the player list
        Game(player_list)

        # prints payer info and resets game value
        for player in player_list:

            player.player_info()
            player.reset_values()
            if player.balance <= 0:
                print("Ending game. One or more player(s) has no remaining funds to play. Thank you for playing Blackjack!")
                quit()
            else:
                continue

    # overall game counter
    game_counter += 1
