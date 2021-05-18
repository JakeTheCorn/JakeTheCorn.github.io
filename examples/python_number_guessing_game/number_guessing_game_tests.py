"""
    TODO:
        √ It writes a welcome message before the game begins
            √ Make writer arg in Game ctor keyword only
            √ Make writer attr in Game appear as non-public
        - It writes a message asking the player to guess a number between 1 and 10
"""

import unittest
from unittest.mock import Mock, call

class NumberGuessingGameTests(unittest.TestCase):
    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        writer = Mock()
        game = Game(
            writer=writer
        )
        game.play()
        self.assertEqual(
            writer.write.mock_calls[0],
            call('Welcome to the number guessing game'),
        )

    def _test_it_writes_a_message_asking_player_to_guess_number_between_1_and_10(self):
        writer = Mock()
        game = Game(
            writer=writer
        )
        game.play()
        writer.write.assert_called_once_with('Please pick a number between 1 and 10')


class Game:
    def __init__(
        self,
        *,
        writer,
    ):
        self._writer = writer

    def play(self):
        self._writer.write('Welcome to the number guessing game')
        self._writer.write('Please pick a number between 1 and 10')

