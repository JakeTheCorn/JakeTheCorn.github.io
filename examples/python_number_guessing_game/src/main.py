import sys
from .game import Game
import random

if sys.argv[1].strip() == 'file':
    from .file import Reader, Writer
else:
    from.console import Reader, Writer

class RandomIntegerGetter:
    def get_random_integer(self):
        return random.randrange(1, 10)

Game(
    reader=Reader(),
    writer=Writer(),
    random_integer_getter=RandomIntegerGetter(),
).play()
