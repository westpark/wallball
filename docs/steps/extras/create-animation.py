#!../code/.venv/scripts/python.exe
import os, sys
import glob
import subprocess

import imageio

IMAGES_DIRPATH = "../images"

def remove_intermediate_images(step):
    for filepath in glob.glob(os.path.join(IMAGES_DIRPATH, "%s.*.png" % step)):
        os.unlink(filepath)

def main(name):
    if not os.path.exists(IMAGES_DIRPATH): os.mkdir(IMAGES_DIRPATH)
    remove_intermediate_images(name)
    subprocess.call(["../code/.venv/scripts/pgzrun.exe", "%s.py" % name])
    files = sorted(glob.glob(os.path.join(IMAGES_DIRPATH, "%s.*.png" % name)))
    try:
        frames = [imageio.imread(f) for f in files]
        imageio.mimsave(os.path.join(IMAGES_DIRPATH, "%s.gif" % name), frames, "GIF", fps=30)
    except:
        raise
    else:
        remove_intermediate_images(name)

if __name__ == '__main__':
    main(*sys.argv[1:])