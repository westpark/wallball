import os, sys
import fnmatch

my_filepath = os.path.abspath(__file__)

for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        filepath = os.path.join(os.path.join(dirpath, filename))
        if filepath == my_filepath:
            continue
        if not filename.endswith(".py"):
            continue

        print(filepath)
        with open(filepath) as f:
            lines = f.readlines()
        with open(filepath, "w") as f:
            f.write("\n".join(l.rstrip() for l in lines))
