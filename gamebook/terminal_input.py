from gamebook.game_input import Input


class TerminalInput(Input):

    def recieve_input(self, prompt):
        data = input(prompt)

        return data
