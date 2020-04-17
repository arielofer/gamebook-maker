from gamebook.output import Output

class TerminalOutput(Output):
    
    def output(self,content):
        print(content)