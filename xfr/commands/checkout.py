from ._base import SubCommand

class CheckoutCommand(SubCommand):
    def __init__(self):
        super().__init__('checkout', 'Switch branches or restore working tree files')
        self.parser.add_argument('branch', help='Branch to checkout')

    def execute(self, args):
        print(f"Switched to branch {args.branch}")

