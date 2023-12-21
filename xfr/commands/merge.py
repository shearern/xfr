from ._base import SubCommand

class MergeCommand(SubCommand):
    def __init__(self):
        super().__init__('merge', 'Join two or more development histories together')
        self.parser.add_argument('branch', help='Branch to merge')

    def execute(self, args):
        print(f"Merged branch {args.branch}")
