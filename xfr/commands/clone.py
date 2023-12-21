from ._base import SubCommand


class CloneCommand(SubCommand):

    def __init__(self):
        super().__init__('clone', 'Clone a repository into a newly created directory')
        self.parser.add_argument('repository', help='URL of the repository to clone')
        self.parser.add_argument('directory', nargs='?', default='.', help='Directory to clone into (default: current directory)')

    def execute(self, args):
        print(f"Cloned repository {args.repository} into directory {args.directory}")

