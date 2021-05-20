import random

class Writer:
    def write(self, msg: str):
        print(msg)

class Reader:
    def read(self) -> str:
        return input()

class RandomIntegerGetter:
    def get_random_integer(self):
        return random.randrange(1, 10)
