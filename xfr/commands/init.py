
from ._base import SubCommand

class InitCommand(SubCommand):

    def __init__(self):
        super().__init__('init', 'Initialize a new XRF repository')
        self.parser.add_argument('url', type=self.repository_path,
            help='Directory to initialize repository storage path')

    def execute(self, args):
        print(f"Initialized a new XRF repository in {args.directory}")
