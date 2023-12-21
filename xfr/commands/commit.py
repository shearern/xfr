from ._base import SubCommand

class CommitCommand(SubCommand):

    def __init__(self):
        super().__init__('commit', 'Record changes to the repository')
        self.parser.add_argument('message', help='Commit message')

    def execute(self, args):
        print(f"Committed changes with message: {args.message}")

