from ._base import SubCommand

class StatusCommand(SubCommand):
    def __init__(self):
        super().__init__('status', 'Show the working tree status')

    def execute(self, args):
        print("Showing the working tree status")

