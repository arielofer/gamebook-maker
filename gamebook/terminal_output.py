from gamebook.output import Output
import os
import sys


class TerminalOutput(Output):
    def output(self, content):
        if content:
            print(content)
        else:
            raise ValueError("no content recieved")

    def clear(self):
        os.system("cls")

    def exit(self, exit_reason):
        self.output(exit_reason)
        sys.exit()
