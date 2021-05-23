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
        self._max_guesses = 3

    def play(self):
        guess_count = 0
        self._writer.write('Welcome to the number guessing game')
        self._write_rules()
        random_number = self._random_integer_getter.get_random_integer()

        while guess_count < self._max_guesses:
            user_guess = self._reader.read().strip()
            if not user_guess.isdigit():
                self._writer.write(f'"{user_guess}" is not a valid integer.')
                self._write_rules()
                continue
            guess_count += 1
            remaining_guesses = self._max_guesses - guess_count
            if user_guess == str(random_number):
                self._writer.write(f'Success! The correct number was {random_number}')
                return

            if remaining_guesses == 0:
                self._writer.write(f'Failure! The correct number was {random_number}')
                return
            guess_string = 'guesses' if remaining_guesses != 1 else 'guess'
            self._writer.write(f'Incorrect! {remaining_guesses} {guess_string} remaining')

    def configure(
        self,
        *,
        max_guesses: int = None,
    ) -> 'Game':
        if isinstance(max_guesses, int):
            self._max_guesses = max_guesses
        return self

    def _write_rules(self):
        self._writer.write('Please pick a number between 1 and 10')


