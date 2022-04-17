import os
import subprocess
import importlib.util as iu
from enum import Enum

GRAMMAR_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/grammar"))
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/python/code/dicetower/"))
MK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

first_run = True


class Mock(Enum):
    NO_MOCK = 0
    RETURN_CONSTANT = 1
    RETURN_INCREMENTING = 2
    RETURN_DECREMENTING = 3
    RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE = 4


def get_roll():

    # We are explicitly using the local module here as we modify the yacc in order to mock our tests.
    # This ugly logic is to bypass the fact that you might have the pip package installed
    # and thus a name conflict
    m = os.path.join(SRC_DIR, "parser.py")
    spec = iu.spec_from_file_location("dt", m)
    dt = iu.module_from_spec(spec)
    spec.loader.exec_module(dt)

    dice_tower_roll = dt.roll
    return dice_tower_roll


def make_clean():
    cmd = "make clean -s -C " + MK_DIR
    cleanup = subprocess.Popen(cmd, shell=True)
    cleanup.communicate()
    if cleanup.returncode:
        raise ValueError


def make_all():
    cmd = "make all -s -C " + MK_DIR
    parser = subprocess.Popen(cmd, shell=True)
    parser.communicate()
    if parser.returncode:
        raise ValueError


def roll(s, mock_mode=Mock.NO_MOCK, mock_const=3):
    global first_run

    if first_run:
        make_clean()
        make_all()
    if mock_mode is None:
        mock_mode = Mock.NO_MOCK
    first_run = False

    # Get module now - post make
    dice_tower_roll = get_roll()
    exit_code, result = dice_tower_roll(s, mock=mock_mode.value, quiet=True, mock_const=mock_const)

    if exit_code:
        raise ValueError
    return result
