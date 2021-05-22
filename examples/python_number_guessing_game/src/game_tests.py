"""
    TODO:
        √ It writes a welcome message before the game begins
        √ It writes a message asking the player to guess a number between 1 and 10
        √ It writes a helpful message if user does not enter a valid integer
        √ It writes a success message if the user inputs a correct guess.
        √ It writes message with Failure and how many guesses left when user is wrong
        √ It automatically ignores leading and trailing whitespace from user input.
        √ It decrements available guesses after multiple wrong guesses
"""

import unittest
import unittest.mock as mock
from .game import Game


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
        self.assertMessages([
            'Welcome to the number guessing game'
        ])

    def test_it_writes_a_message_asking_player_to_guess_number_between_1_and_10(self):
        self.game.play()
        self.assertMessages([
            'Welcome to the number guessing game',
            'Please pick a number between 1 and 10'
        ])

    def test_it_writes_a_helpful_message_if_user_does_not_enter_valid_integer(self):
        for user_guess in [
            'Hello',
            'Goodbye',
            '1.1',
        ]:
            self.setUp()
            # bad guess followed by three valid guesses to avoid test hanging
            self.reader.read.side_effect = [user_guess, '1', '2', '3']
            with self.subTest(user_guess):
                self.game.play()
                self.assertMessages([
                    'Welcome to the number guessing game',
                    'Please pick a number between 1 and 10',
                    f'"{user_guess}" is not a valid integer.',
                    'Please pick a number between 1 and 10',
                ])

    def test_it_writes_a_success_message_if_user_inputs_correct_guess(self):
        self.reader.read.side_effect = ['5']
        self.random_integer_getter.get_random_integer.return_value = 5
        self.game.play()
        self.assertMessages([
            'Welcome to the number guessing game',
            'Please pick a number between 1 and 10',
            'Success! The correct number was 5',
        ])

    def test_it_writes_incorrect_with_how_many_guesses_remain_when_incorrect_guess(self):
        self.reader.read.return_value = '4'
        self.random_integer_getter.get_random_integer.return_value = 2
        self.game.play()
        self.assertMessages([
            'Welcome to the number guessing game',
            'Please pick a number between 1 and 10',
            'Incorrect! 2 guesses remaining',
        ])

    def test_it_ignores_trailing_and_leading_whitespace_from_user_input(self):
        self.reader.read.return_value = ' 3  \n '
        self.random_integer_getter.get_random_integer.return_value = 3
        self.game.play()
        self.assertMessages([
            'Welcome to the number guessing game',
            'Please pick a number between 1 and 10',
            'Success! The correct number was 3',
        ])

    def test_it_decrements_available_guesses_after_multiple_wrong_guesses(self):
        self.reader.read.side_effect = ['1', '2', '3']
        self.random_integer_getter.get_random_integer.return_value = 4
        self.game.play()
        self.assertMessages([
            'Welcome to the number guessing game',
            'Please pick a number between 1 and 10',
            'Incorrect! 2 guesses remaining',
            'Incorrect! 1 guess remaining',
            'Failure! The correct number was 4',
        ])

    # helpers
    def assertMessages(self, messages: list[str]) -> None:
        for idx, msg in enumerate(messages):
            self.assertEqual(
                mock.call(msg),
                self.writer.write.mock_calls[idx],
            )
