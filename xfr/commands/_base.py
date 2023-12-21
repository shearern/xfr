from abc import ABC, abstractmethod
import urllib.parse
import argparse

# === Command Handlers =========================================================


class XFR_Command:
    ROOT_PARSER = argparse.ArgumentParser(description='XRF command-line tool', prog='xfr')
    SUBPARSERS = ROOT_PARSER.add_subparsers(title='Sub-Command', dest='command')
    SUBPARSERS.required = True  # Require a sub-command

    @classmethod
    def execute(cls, argv):
        cls.ROOT_PARSER.parse_args(argv)


class SubCommand(ABC):

    def __init__(self, name, help):
        self.name = name
        self.help = help
        self.parser = XFR_Command.SUBPARSERS.add_parser(name, help=help)
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

