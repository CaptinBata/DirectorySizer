"""App that calculates size of given directory."""

import sys
from pathlib import Path

from folder import Folder

args = sys.argv
path = ""
verbose = False
scalor = "B"
allowed_scalors = ["B", "KB", "MB", "GB", "TB"]


def assign_args(args):
    """Assign the passed in args."""
    global path
    global scalor
    global verbose

    if len(args) > 1:
        for i in range(1, len(args)):
            if args[i] in allowed_scalors:
                scalor = args[i]
            elif args[i] == "-v":
                verbose = True
            else:
                path = str(Path(args[i]).resolve())
                print(f"Path: {path}")
    else:
        path = str(Path(args[0]).resolve())


assign_args(args)

directory = Folder(path, scalor, verbose=verbose)

directory.start()
