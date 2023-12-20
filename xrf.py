"""
xrf.py - A git-like tool for managing repositories of large files
"""
import urllib
from abc import ABC, abstractmethod
import argparse


# === Command Handlers =========================================================

ROOT_PARSER = argparse.ArgumentParser(description='XRF command-line tool')
SUBPARSERS = ROOT_PARSER.add_subparsers(title='Operations', dest='operation')
SUBPARSERS.required = True  # Require a sub-command


class Command(ABC):

    def __init__(self, name, help):
        self.parser = SUBPARSERS.add_parser(name, help=help)
        self.parser.set_defaults(func=self.execute)


    def repository_path(self, value):
        """Command parameter that refers to a repository path"""
        # Absolute path
        parts = urllib.parse.urlparse(value)
        if parts.scheme != 'xrf':
            raise argparse.ArgumentTypeError(f"Invalid repository path: {value}")
        return value

    @abstractmethod
    def execute(self, args):
        pass


class InitCommand(Command):

    def __init__(self):
        super().__init__('init', 'Initialize a new XRF repository')
        self.parser.add_argument('url', type=self.repository_path,
            help='Directory to initialize repository storage path')

    def execute(self, args):
        print(f"Initialized a new XRF repository in {args.directory}")

class CommitCommand(Command):

    def __init__(self):
        super().__init__('commit', 'Record changes to the repository')
        self.parser.add_argument('message', help='Commit message')

    def execute(self, args):
        print(f"Committed changes with message: {args.message}")

class PushCommand(Command):
    def __init__(self):
        super().__init__('push', 'Push changes to the remote repository')
        self.parser.add_argument('remote', help='Name of the remote repository')

    def execute(self, args):
        print(f"Pushed changes to remote repository: {args.remote}")

class CloneCommand(Command):
    def __init__(self):
        super().__init__('clone', 'Clone a repository into a newly created directory')
        self.parser.add_argument('repository', help='URL of the repository to clone')
        self.parser.add_argument('directory', nargs='?', default='.', help='Directory to clone into (default: current directory)')

    def execute(self, args):
        print(f"Cloned repository {args.repository} into directory {args.directory}")

class AddCommand(Command):
    def __init__(self):
        super().__init__('add', 'Add file contents to the index')
        self.parser.add_argument('file', nargs='+', help='File(s) to add')

    def execute(self, args):
        print(f"Added file(s) {args.file} to the index")

class StatusCommand(Command):
    def __init__(self):
        super().__init__('status', 'Show the working tree status')

    def execute(self, args):
        print("Showing the working tree status")

class LogCommand(Command):
    def __init__(self):
        super().__init__('log', 'Show commit logs')

    def execute(self, args):
        print("Showing commit logs")

class CheckoutCommand(Command):
    def __init__(self):
        super().__init__('checkout', 'Switch branches or restore working tree files')
        self.parser.add_argument('branch', help='Branch to checkout')

    def execute(self, args):
        print(f"Switched to branch {args.branch}")

class BranchCommand(Command):
    def __init__(self):
        super().__init__('branch', 'List, create, or delete branches')

    def execute(self, args):
        print("Listing, creating, or deleting branches")

class MergeCommand(Command):
    def __init__(self):
        super().__init__('merge', 'Join two or more development histories together')
        self.parser.add_argument('branch', help='Branch to merge')

    def execute(self, args):
        print(f"Merged branch {args.branch}")

class PullCommand(Command):
    def __init__(self):
        super().__init__('pull', 'Fetch from and integrate with another repository or a local branch')
        self.parser.add_argument('remote', help='Name of the remote repository')

    def execute(self, args):
        print(f"Pulled changes from remote repository {args.remote}")


# === Main =====================================================================

COMMANDS = [
    InitCommand(),
    CommitCommand(),
    PushCommand(),
    CloneCommand(),
    AddCommand(),
    StatusCommand(),
    LogCommand(),
    CheckoutCommand(),
    BranchCommand(),
    MergeCommand(),
    PullCommand(),
]


if __name__ == '__main__':
    args = ROOT_PARSER.parse_args()
    args.func(args)

