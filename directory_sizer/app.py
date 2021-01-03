"""App that calculates size of given directory."""

import sys
from pathlib import Path

from folder import Folder

args = sys.argv
path = ""
verbose = False
scalor = "B"

if len(args) == 4:
    path = str(Path(args[1]).resolve())  # index 1 because 0 is the script name
    verbose = True if args[3] == "-v" else False
    scalor = args[2]
if len(args) == 3:
    path = str(Path(args[1]).resolve())  # index 1 because 0 is the script name
    scalor = args[2]
elif len(args) == 2:
    path = str(Path(args[1]).resolve())  # index 1 because 0 is the script name
elif len(args) == 1:
    path = str(Path(args[0]).resolve())

directory = Folder(path, scalor, verbose=verbose)

print("Scanning provided directory")
directory.scan()
print("Calculating size of directory")
directory.calculate_size()
print("Outputting findings into text file in passed directory")
directory.output()
