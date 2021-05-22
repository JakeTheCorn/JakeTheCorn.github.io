class Reader:
    def __init__(self) -> None:
        with open('./src/file/in_file') as f:
            self.guesses = f.read().split(',')
        self.current_idx = 0

    def read(self):
        guess = self.guesses[self.current_idx].strip()
        self.current_idx += 1
        return guess

class Writer:
    def write(self, msg: str) -> None:
        with open('./src/file/out_file', 'a') as f:
            f.write(msg + '\n')
