import os, sys
import glob
import subprocess

import imageio

IMAGES_DIRPATH = "../images"

def remove_intermediate_images(step):
    for filepath in glob.glob(os.path.join(IMAGES_DIRPATH, "%s.*.png" % step)):
        os.unlink(filepath)

def main(step):
    if not os.path.exists(IMAGES_DIRPATH): os.mkdir(IMAGES_DIRPATH)
    remove_intermediate_images(step)
    subprocess.call([".venv\scripts\pgzrun", "%s.py" % step])
    files = sorted(glob.glob(os.path.join(IMAGES_DIRPATH, "%s.*.png" % step)))
    try:
        frames = [imageio.imread(f) for f in files]
        imageio.mimsave(os.path.join(IMAGES_DIRPATH, "step-%s.gif" % step), frames, "GIF", fps=90)
    except:
        raise
    else:
        remove_intermediate_images(step)

if __name__ == '__main__':
    main(*sys.argv[1:])