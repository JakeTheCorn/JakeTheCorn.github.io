class Game:
    def __init__(
        self,
        *,
        reader,
        writer,
        random_integer_getter,
    ):
        self._reader = reader
        self._writer = writer
        self._random_integer_getter = random_integer_getter

    def play(self):
        MAX_GUESSES = 3
        guess_count = 0

        self._writer.write('Welcome to the number guessing game')
        self._write_rules()
        random_number = self._random_integer_getter.get_random_integer()

        while guess_count < MAX_GUESSES:
            user_guess = self._reader.read().strip()

            if not user_guess.isdigit():
                self._writer.write(f'"{user_guess}" is not a valid integer.')
                self._write_rules()
                continue
            guess_count += 1
            remaining_guesses = MAX_GUESSES - guess_count
            if user_guess == str(random_number):
                self._writer.write(f'Success! The correct number was {random_number}')
                return
            else:
                if remaining_guesses == 0:
                    self._writer.write(f'Failure! The correct number was {random_number}')
                    return
                guess_string = 'guesses' if remaining_guesses != 1 else 'guess'
                self._writer.write(f'Incorrect! {remaining_guesses} {guess_string} remaining')

    def _write_rules(self):
        self._writer.write('Please pick a number between 1 and 10')

if __name__ == '__main__':
    from .console import Writer, Reader, RandomIntegerGetter
    import os
    from .file import Writer, Reader, RandomIntegerGetter
    import sys

    if sys.argv[1] == 'file':
        from .file import Writer, Reader, RandomIntegerGetter
        writer=Writer(
            filepath=os.path.abspath('./logs')
        )
        reader=Reader(
            filepath=os.path.abspath('./my_guesses')
        )
        random_integer_getter=RandomIntegerGetter()
    else:
        from .console import Writer, Reader, RandomIntegerGetter
        writer=Writer()
        reader=Reader()
        random_integer_getter=RandomIntegerGetter()

    Game(
        writer=writer,
        reader=reader,
        random_integer_getter=random_integer_getter
    ).play()
