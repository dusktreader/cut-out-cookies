"""
This is necessary to call in a post-gen hook due to:
https://stackoverflow.com/a/57892171/642511
"""
import pathlib

from cutout.constants import STENCIL_PATH_PREFIX


def rm_tree(path: pathlib.Path):
    """
    Stolen shamelessly from:
    https://stackoverflow.com/a/57892171/642511
    """
    for child in path.iterdir():
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    path.rmdir()


def cleanup():
    for match in pathlib.Path().glob(f"**/{STENCIL_PATH_PREFIX}*"):
        if match.is_dir():
            rm_tree(match)
