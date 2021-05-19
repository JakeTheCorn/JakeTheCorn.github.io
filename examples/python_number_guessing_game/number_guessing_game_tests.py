"""
    TODO:
        √ It writes a welcome message before the game begins
            √ Make writer arg in Game ctor keyword only
            √ Make writer attr in Game appear as non-public
        √ It writes a message asking the player to guess a number between 1 and 10
            √ Revisit the tests knowing about order of writer calls
            √ DRY common test arrage/setup steps
            √ put expectation on left side of assertEqual
            √ use mock.call() instead of call() to make meaningful distinction in calling code
        √ It writes a helpful message if user does not enter a valid integer
        √ It writes a success message if the user inputs a correct guess.
        - When user inputs valid integer
          - When it is an incorrect guess
            - Then it writes a message saying incorrect
            - Then it writes a message about how many guesses left
"""

import unittest
import unittest.mock as mock


class NumberGuessingGameTests(unittest.TestCase):
    def setUp(self):
        self.writer = mock.Mock()
        self.reader = mock.Mock()
        self.random_integer_getter = mock.Mock()
        self.game = Game(
            reader=self.reader,
            writer=self.writer,
            random_integer_getter=self.random_integer_getter,
        )

    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        self.game.play()
        first_call = self.writer.write.mock_calls[0]
        self.assertEqual(
            mock.call('Welcome to the number guessing game'),
            first_call,
        )

    def test_it_writes_a_message_asking_player_to_guess_number_between_1_and_10(self):
        self.game.play()
        second_call = self.writer.write.mock_calls[1]
        self.assertEqual(
            mock.call('Please pick a number between 1 and 10'),
            second_call,
        )

    def test_it_writes_a_helpful_message_if_user_does_not_enter_valid_integer(self):
        for user_guess in [
            'Hello',
            'Goodbye',
            '1.1',
        ]:
            self.setUp()
            with self.subTest(user_guess):
                self.reader.read.return_value = user_guess
                self.game.play()
                second_to_last_write_call = self.writer.write.mock_calls[-2]
                last_write_call = self.writer.write.mock_calls[-1]

                self.reader.read.assert_called_once()
                self.assertEqual(
                    mock.call(f'"{user_guess}" is not a valid integer.'),
                    second_to_last_write_call,
                )
                self.assertEqual(
                    mock.call('Please pick a number between 1 and 10'),
                    last_write_call,
                )

    def test_it_writes_a_success_message_if_user_inputs_correct_guess(self):
        self.reader.read.return_value = '5'
        self.random_integer_getter.get_random_integer.return_value = 5
        self.game.play()
        last_write_call = self.writer.write.mock_calls[-1]
        self.reader.read.assert_called_once()
        self.assertEqual(
            mock.call('Success! The correct number was 5'),
            last_write_call,
        )

    def test_it_writes_incorrect_with_how_many_guesses_remain_when_incorrect_guess(self):
        self.reader.read.return_value = '4'
        self.game.play()
        last_write_call = self.writer.write.mock_calls[-1]
        self.assertEqual(
            mock.call('Incorrect! 2 guesses remaining'),
            last_write_call
        )


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
        self._writer.write('Welcome to the number guessing game')
        self._write_rules()
        random_number = self._random_integer_getter.get_random_integer()
        user_guess = self._reader.read()
        if not user_guess.isdigit():
            self._writer.write(f'"{user_guess}" is not a valid integer.')
            self._write_rules()
            return
        if user_guess == str(random_number):
            self._writer.write(f'Success! The correct number was {random_number}')
        else:
            self._writer.write('Incorrect! 2 guesses remaining')

    def _write_rules(self):
        self._writer.write('Please pick a number between 1 and 10')
