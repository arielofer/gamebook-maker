from gamebook.terminal_input import TerminalInput
import pytest


def test_if_data_is_recieved(monkeypatch):
    path = 'gamebook.terminal_input.TerminalInput.recieve_input'
    monkeypatch.setattr(path, lambda self, prompt: "east")
    instance_input = TerminalInput()

    answer = instance_input.recieve_input("east or west?")

    assert answer == "east"
