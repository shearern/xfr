from ._base import SubCommand

class PushCommand(SubCommand):
    def __init__(self):
        super().__init__('push', 'Push changes to the remote repository')
        self.parser.add_argument('remote', help='Name of the remote repository')

    def execute(self, args):
        print(f"Pushed changes to remote repository: {args.remote}")

