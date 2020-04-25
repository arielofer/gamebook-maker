from gamebook.terminal_input import TerminalInput
import pytest


def test_is_input_recieved():
    instance_input = TerminalInput()

    data = instance_input.recieve_input("ma name jeff")

    assert data == "otis son"
