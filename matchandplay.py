#Play a card game called Match and Play.
#GamePlay: 
#52 cards are shuffled in a deck.
#Five cards are given to each player.
#The top card from the deck is discarded to decide the opening suit.

#Player Turns:
#Players take turns in a clockwise direction.

#During a player's turn, they can play a card if it matches the suit or rank of the top card from the discard pile.
#Draw a Card: If no playable cards are available, the player selects one from the deck.
#The first player to play all of their cards wins the game!

#Powers & Features

#Queen (Draw One Card):
#When a Queen is played, the next player must draw one extra card from the deck.
#Ace (Reverse Direction):
#Playing an Ace changes the direction of play (clockwise to anti-clockwise or vice versa).
#Jack (Suit Switcher):
#Playing a Jack allows the player to change the current suit to any other suit of their choice.


#Special Features of "Match and Play"

#1. Strategic Suit Changes: 
#     By playing a Jack, players can strategically change their current suit, potentially forcing opponents to draw cards if they don't have a matching suit.

#2. Unpredictable Gameplay
#     Power cards such as Queens, Aces, and Jacks add unpredictability. Queens force the next player to draw an additional card, Aces reverse the direction of play, and Jacks switch suits.

#3. Simple Rules and Quick Setup
#     The game is simple to learn and set up. Players receive five cards, and the goal is to be the first to play all of their cards.

#4. Dynamic Winning Conditions: 
#     The first player to play all their cards wins, but strategic use of power cards can change the game's outcome at any time.
















#CODE:

import random

class CardGame:
    def __init__(self, rank, suit):
        # Represents a single playing card with a specific rank and suit.
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        # Returns a string representation of the card.
        return f"{self.rank} of {self.suit}"

class DeckOfCards:
    def __init__(self):
        # Defines the deck of cards with suits and ranks, then initializes and shuffles them.
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = []  # List to hold all the cards.

        # Create the deck using nested loops to generate each card.
        for suit in suits:
            for rank in ranks:
                self.cards.append(CardGame(rank, suit))

        # Shuffle the deck to randomize the card order.
        random.shuffle(self.cards)

    def draw_card(self):
        # Draws the top card from the deck, if available, or returns None if the deck is empty.
        return self.cards.pop() if self.cards else None

class PlayerInGame:
    def __init__(self, name):
        # Represents a player with a hand of cards and methods to draw and play cards.
        self.name = name
        self.hand = []

    def manage_cards(self, deck, action, card_index=None):
        # Handles drawing and playing cards for the player.
        if action == 'draw':
            card = deck.draw_card()
            if card:
                self.hand.append(card)
                return f"Drawn: {card}"
            return "Deck is empty. No card drawn."
        elif action == 'play' and card_index is not None:
            if 0 <= card_index < len(self.hand):
                return self.hand.pop(card_index)
            return "Invalid card index."
        return "Invalid action or missing card index for 'play'."

class Game:
    def __init__(self, players):
        # Controls the gameplay logic for Crazy Eights, managing players, turns, and the deck.
        self.deck = DeckOfCards()
        self.players = [PlayerInGame(name) for name in players]
        self.discard_pile = []
        self.current_suit = None
        self.deal_cards()  # Initialize by dealing cards

    def deal_cards(self):
        # Shuffles the deck and deals 5 cards to each player, starting the discard pile.
        random.shuffle(self.deck.cards)
        for player in self.players:
            player.hand = [self.deck.draw_card() for _ in range(5)]
        # Place one card in the discard pile
        top_card = self.deck.draw_card()
        self.discard_pile.append(top_card)
        # Set the current suit to the suit of the card in the discard pile
        self.current_suit = top_card.suit

    def play_power_card(self, card):
        # Implements special effects for power cards like drawing cards or reversing play direction.
        if card.rank == 'Queen':
            print(f"Next player must draw one card. (Power Card Effect)")
            return "draw_one"
        elif card.rank == 'Ace':
            print(f"Direction of play changes. (Power Card Effect)")
            return "reverse"
        return "normal"

    def strategic_suit_change(self, card):
        # Allows the player to change the current suit when a 'Jack' is played.
        if card.rank == 'Jack':
            new_suit = input("Enter new suit (Hearts, Diamonds, Clubs, Spades): ").strip().capitalize()
            while new_suit not in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                new_suit = input("Invalid suit. Enter new suit (Hearts, Diamonds, Clubs, Spades): ").strip().capitalize()
            self.discard_pile[-1].suit = new_suit  # Change the suit of the card in the discard pile.
            print(f"Suit changed to {new_suit} by playing a Jack.")
            return new_suit
        return card.suit

    def is_playable(self, card):
        # Determines if a card can be played based on the top card of the discard pile.
        return card.rank == 'Jack' or card.suit == self.discard_pile[-1].suit or card.rank == self.discard_pile[-1].rank

    def start_game(self):
        # Starts the main game loop, managing player turns and applying game rules.
        current_player = 0
        direction = 1  # 1 : clockwise, -1 : anticlockwise
        while True:
            player = self.players[current_player]
            playable_cards = [card for card in player.hand if self.is_playable(card)]

            if not playable_cards:
                player.manage_cards(self.deck, 'draw')
                current_player = (current_player + direction) % len(self.players)
                continue

            print(f"{player.name}'s turn. Hand: {player.hand}")
            print(f"Top of discard pile: {self.discard_pile[-1]}")
            try:
                card_index = int(input("Choose index of the card: "))
                if not (0 <= card_index < len(player.hand)):
                    raise ValueError
            except (ValueError, IndexError):
                print("Invalid index. Try again.")
                continue

            chosen_card = player.manage_cards(self.deck, 'play', card_index)
            print(f"{player.name} played: {chosen_card}")

            effect = self.play_power_card(chosen_card)
            if effect == "reverse":
                direction *= -1
                
            elif effect == "draw_one":
                next_player = (current_player + direction) % len(self.players)
                self.players[next_player].manage_cards(self.deck, 'draw')

            self.current_suit = self.strategic_suit_change(chosen_card)  # Apply suit change if a Jack was played.
            self.discard_pile.append(chosen_card)

            if not player.hand:
                print(f"{player.name} wins!")
                break

            current_player = (current_player + direction) % len(self.players)

# Start the game by creating a Game object with a list of player names and calling start_game.
if __name__ == "__main__":
    game = Game(["Chandu", "Ammu"])
    game.start_game()
