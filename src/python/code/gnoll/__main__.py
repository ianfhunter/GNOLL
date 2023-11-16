'''Roll some dice with GNOLL.'''

import sys, argparse, gnoll

def parse_cmdline_args(args):
    p = argparse.ArgumentParser(
        description = __doc__,
        usage = 'python3 -m gnoll [options] EXPR',
        add_help = False)

    p.add_argument('EXPR', nargs = '+',
        help = 'a dice expression to evaluate '
            '(multiple arguments will be joined with spaces)')

    g = p.add_argument_group('main options')
    g.add_argument('-h', '--help', action = 'help',
        help = 'show this help message and exit')
    g.add_argument('-b', '--breakdown', action = 'store_true',
        help = 'show a breakdown into individual dice')
    g.add_argument('--no-builtins', action = 'store_true',
        help = 'disable built-in macros')

    g = p.add_argument_group('debugging options')
    g.add_argument('-v', '--verbose', action = 'store_true',
        help = 'enable verbosity')
    g.add_argument('--keep-temp-file', action = 'store_true',
        help = "don't delete the created temporary file")
    g.add_argument('--mock', metavar = 'TYPE', type = int,
        help = 'mocking type')
    g.add_argument('--mock-const', metavar = 'N', type = int, default = 3,
        help = 'mocking constant')

    a = p.parse_args(args)
    a.EXPR = ' '.join(a.EXPR)
    return a

def main(EXPR, no_builtins, **kwargs):
    _, [[result]], breakdown = gnoll.roll(
        EXPR,
        builtins = not no_builtins,
        **kwargs)
    if breakdown:
        print(breakdown[0], '-->', result)
    else:
        print(result)

if __name__ == '__main__':
    main(**vars(parse_cmdline_args(sys.argv[1:])))