import os, sys

from xfr.commands import XFR_Command

if __name__ == '__main__':
    args = XFR_Command.parse_and_execute(sys.argv[1:])