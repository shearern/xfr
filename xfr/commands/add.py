from ._base import SubCommand

class AddCommand(SubCommand):

    def __init__(self):
        super().__init__('add', 'Add file contents to the index')
        self.parser.add_argument('file', nargs='+', help='File(s) to add')

    def execute(self, args):
        print(f"Added file(s) {args.file} to the index")

