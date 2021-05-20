import random
from itertools import islice

class Writer:
    def __init__(
        self,
        *,
        filepath: str
    ) -> None:
        self._filepath = filepath

    def write(self, msg: str):
        with open(self._filepath, 'a') as f:
            f.write(msg + '\n')


class Reader:
    def __init__(
        self,
        *,
        filepath: str
    ) -> None:
        self.current_idx = 0
        self._filepath = filepath

    def read(self) -> str:
        with open(self._filepath) as f:
            for line in islice(f, self.current_idx, self.current_idx + 1):
                return line.strip()

class RandomIntegerGetter:
    def get_random_integer(self):
        return random.randrange(1, 10)
