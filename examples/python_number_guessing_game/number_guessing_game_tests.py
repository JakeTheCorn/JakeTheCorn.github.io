"""
    TODO:
        √ It writes a welcome message before the game begins
            √ Make writer arg in Game ctor keyword only
            √ Make writer attr in Game appear as non-public
"""

import unittest
from unittest.mock import Mock

class NumberGuessingGameTests(unittest.TestCase):
    def test_it_writes_a_welcome_message_before_the_game_begins(self):
        writer = Mock()
        game = Game(
            writer=writer
        )
        game.play()
        writer.write.assert_called_once_with('Welcome to the number guessing game')


class Game:
    def __init__(
        self,
        *,
        writer,
    ):
        self._writer = writer

    def play(self):
        self._writer.write('Welcome to the number guessing game')

