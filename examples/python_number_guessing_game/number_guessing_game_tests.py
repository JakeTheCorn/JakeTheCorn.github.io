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
        - It writes a helpful message if user does not enter a valid integer
"""

import unittest
import unittest.mock as mock


class NumberGuessingGameTests(unittest.TestCase):
    def setUp(self):
        self.writer = mock.Mock()
        self.reader = mock.Mock()
        self.game = Game(
            reader=self.reader,
            writer=self.writer,
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
        self.game.play()
        second_to_last_write_call = self.writer.write.mock_calls[-2]
        last_write_call = self.writer.write.mock_calls[-1]

        self.reader.read.assert_called_once()
        self.assertEqual(
            mock.call('"Hello" is not a valid integer.'),
            second_to_last_write_call,
        )
        self.assertEqual(
            mock.call('Please pick a number between 1 and 10'),
            last_write_call,
        )


class Game:
    def __init__(
        self,
        *,
        reader,
        writer,
    ):
        self._reader = reader
        self._writer = writer

    def play(self):
        self._writer.write('Welcome to the number guessing game')
        self._writer.write('Please pick a number between 1 and 10')
        user_guess = self._reader.read()
        print(user_guess)
