from card import *
class Deck:
    def __init__(self):
        self._deck = set(Card("hui", "asdfasdf.png", 100, 100, "desc", 2, lambda a: a+1, lambda b: b+1))
