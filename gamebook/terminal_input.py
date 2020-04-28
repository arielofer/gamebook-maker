from gamebook.game_input import Input


class TerminalInput(Input):

    def input(self, prompt):
        data = input(prompt)

        return data

    def ask_for_user_inputs(self, option):
        input("please enter one of the following "+option.show_user_inputs())
