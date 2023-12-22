import os
import argparse


def existing_directory(path):
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"Directory does not exist: {path}")
    return path
