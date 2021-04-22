from gamebook.input_interface import InputInterface
from gamebook.constants import exit_user_input_request, input_prompt
from gamebook.constants import user_inputs_request_format


class TerminalInput(InputInterface):

    def input(self, prompt: str) -> str:
        data = input(prompt)

        return data

    def ask_for_user_inputs(self, options: list) -> str:
        user_inputs_string = "\n"
        for option in options:
            user_inputs_string += user_inputs_request_format.format(
                option_title=option.show_title(),
                option_user_inputs=option.show_user_inputs())

        user_inputs_string += f"{exit_user_input_request}\n\n"
        user_input = input(user_inputs_string + input_prompt)

        return user_input
