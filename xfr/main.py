import os, sys

from xfr.commands import XFR_Command

if __name__ == '__main__':
    XFR_Command.execute(sys.argv[1:])