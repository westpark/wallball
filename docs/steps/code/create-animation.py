import os, sys
import glob
import subprocess

import imageio

def main(step):
    if not os.path.exists("images"): os.mkdir("images")
    subprocess.call(["pgzrun", "--screenshots=images/%s" % step, "%s.py" % step])
    files = sorted(glob.glob("images/%s*.jpg" % step))
    frames = [imageio.imread(f) for f in files]
    imageio.mimsave("step-%s.gif" % step, frames, "GIF", fps=90)

if __name__ == '__main__':
    main(*sys.argv[1:])