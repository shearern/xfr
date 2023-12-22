import sys
from abc import ABC, abstractmethod
import urllib.parse
import argparse


class AbortCommand(Exception): pass


class XFR_Command:
    ROOT_PARSER = argparse.ArgumentParser(description='XRF command-line tool', prog='xfr')
    SUBPARSERS = ROOT_PARSER.add_subparsers(title='Sub-Command', dest='command')
    SUBPARSERS.required = True  # Require a sub-command

    @staticmethod
    def parse(argv):
        return XFR_Command.ROOT_PARSER.parse_args(argv)

    @staticmethod
    def parse_and_execute(argv):
        args = XFR_Command.parse(argv)
        try:
            args.func(args)
        except AbortCommand as e:
            print(f"ERROR: {e}")
            sys.exit(2)



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

