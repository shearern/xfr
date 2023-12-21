
from ._base import SubCommand

class BranchCommand(SubCommand):
    def __init__(self):
        super().__init__('branch', 'List, create, or delete branches')

    def execute(self, args):
        print("Listing, creating, or deleting branches")

