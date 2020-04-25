from gamebook.output import Output
import os


class TerminalOutput(Output):
    def output(self, content):
        if content:
            print(content)
        else:
            raise ValueError("no content recieved")

    def clear(self):
        os.system("cls")
