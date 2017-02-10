import os, sys
import glob

for filepath in glob.glob("s??.py"):
    print(filepath)
    with open(filepath) as f:
        lines = f.readlines()
    with open(filepath, "w") as f:
        f.write("\n".join(l.rstrip() for l in lines))
