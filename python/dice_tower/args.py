from random import choice
import argparse

from dice_tower.meta import ArgumentError

def not_random_lowest(data):
    return data[0]


def not_random_highest(data):
    return data[-1]


def choose_item(items):
    # Random
    return choice(items)


def setup_arguments():

    parser = argparse.ArgumentParser(description='Dice Tower. Use it to roll dice.')
    parser.add_argument('roll_string', action='store',
                        help="The dice roll to evaluate")
    parser.add_argument('--verbose', action='store_true',
                        help='Prints a lot of debug information. Used for development and/or bug reporting')
    parser.add_argument('--silent', action='store_true',
                        help='Avoids printing aside from result reporting at all costs. Even on error')
    parser.add_argument('--force-max', action='store_true',
                        help='Forces the random backend to always choose the highest value')
    parser.add_argument('--force-min', action='store_true',
                        help='Forces the random backend to always choose the lowest value')
    parser.add_argument('--no-macros', action='store_false', dest='macros',
                        help='Disables loading of pre-written macros')
    args = parser.parse_args()
    return args


def validate_args(args):
    if args.force_max and args.force_min:
        raise ArgumentError
    if args.verbose and args.silent:
        raise ArgumentError


def reformat_args(a):
    if a.verbose:
        a.verbosity = "DEBUG"
    elif a.silent:
        a.verbosity = "SILENT"
    else:
        a.verbosity = "WARN"

    if a.force_max:
        a.rand_fn = not_random_highest
    elif a.force_min:
        a.rand_fn = not_random_lowest
    else:
        a.rand_fn = choose_item

    return a