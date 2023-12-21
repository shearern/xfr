from ._base import SubCommand

class LogCommand(SubCommand):
    def __init__(self):
        super().__init__('log', 'Show commit logs')

    def execute(self, args):
        print("Showing commit logs")
