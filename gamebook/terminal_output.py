from gamebook.output import Output


class TerminalOutput(Output):
    def output(self, content):
        if content:
            print(content)
        else:
            print("no content recieved")
