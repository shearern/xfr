from ._base import SubCommand

class IgnoreCommand(SubCommand):

    def __init__(self):
        super().__init__('ignore', 'Mark a file to be ignored in the project')

    def execute(self, args):
        print(f"Committed changes with message: {args.message}")

