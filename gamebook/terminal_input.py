from gamebook.game_input import Input
from gamebook.important_strings import exit_user_input


class TerminalInput(Input):

    def input(self, prompt):
        data = input(prompt)

        return data

    def ask_for_user_inputs(self, options):
        user_input_string = "\n"
        for option in options:
            user_input_string += (f"to {option.show_title()} enter one of the"
                                  f" following {option.show_user_inputs()}\n")
        user_input_string += f"to exit the game enter: {exit_user_input}\n\n"
        user_input = input(user_input_string + "your choice:")

        return user_input
