import pygame
import sys
import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.sprite = f"assets/card/png/{value}_of_{suit.lower()}.png"
        self.image = pygame.image.load(self.sprite)

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def show(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()
    
    def draw_animated(self, screen, x, y):
        card = self.cards.pop()
        screen.blit(card.image, (x, y))
        return card
    
    def draw_multiple(self, num):
        cards = []
        for _ in range(num):
            cards.append(self.cards.pop())
        return cards
    
    def draw_multiple_animated(self, screen, x, y, num):
        cards = []
        for _ in range(num):
            card = self.cards.pop()
            screen.blit(card.image, (x, y))
            cards.append(card)
            x += 20
        return cards


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def showHand(self):
        for card in self.hand:
            print(card)

    def discard(self):
        return self.hand.pop()


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player("Player1")

    def run(self):
        for i in range(5):
            self.player.draw(self.deck)
        self.player.showHand()

        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Card Game")
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            for i, card in enumerate(self.player.hand):
                screen.blit(card.image, (i * 100, 200))
                # add background color white to the card
                pygame.draw.rect(screen, (255, 255, 255), (i * 100, 200, 100, 150), 2)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
