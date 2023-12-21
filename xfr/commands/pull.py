from ._base import SubCommand

class PullCommand(SubCommand):
    def __init__(self):
        super().__init__('pull', 'Fetch from and integrate with another repository or a local branch')
        self.parser.add_argument('remote', help='Name of the remote repository')

    def execute(self, args):
        print(f"Pulled changes from remote repository {args.remote}")
