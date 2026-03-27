
#---------------------- SPECIAL METHODS----------------------#


"""
    Special methods (aka dunder methods) such as .__len__() and .__getitem__() allow you to utilize native Python functionality
in your custom classes. For example:

"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self): # This allows us to do len(FrenchDeck), rather than something like FrenchDeck.length()
        return len(self._cards)

    def __getitem__(self, index): # this allows us to do FrenchDeck[0] to return the first card, and all other bracket
        return self._cards[index] # syntax operations ([::-1], etc), as well as makes the FrenchDeck class iterable.

"""
    Beyond specific Pythonic operations, special methods allow our custom class to interact cleanly with
    the Python standard library, and behave like a standard python object. We can now use random.choice() 
    from the random module on our class to retrieve a random card, thanks to the __getitem__() special method!
"""

# NOTE: Special methods are to be identified and called by the interpreter, not by you!
# DO NOT do deck.__len()__, but len(deck)

# IN PRACTICE:
import random

deck = FrenchDeck()
print(f"Our deck is {len(deck)} cards long.")
print(f"Random card: {random.choice(deck)}")
print(f"Cards in reverse: {deck[::-1]}")

for i in deck:
    if i.rank == "J":
        print(f"JACK!!: {i}")
    else:
        continue


# ------ Additional Notes ------
"""
- The len() function works differently for built-in types like list, str, dict written in C.
    Instead of calling the method, the interpreter reads a field called "ob_size" of the C struct that defines
    native collections. This is more efficient than calling the method.
"""