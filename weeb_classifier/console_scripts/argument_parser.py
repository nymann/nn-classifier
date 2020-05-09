"""
This module is used for defining which command line arguments the user should be able to provide.
"""
from argparse import ArgumentParser, Namespace


def default() -> Namespace:
    """
    Specifies the command line arguments the user is able to provide.
    :return: Namespace
    """
    parser = ArgumentParser()
    parser.add_argument('images', metavar='I', type=str, nargs='+',
                        help='One or more images to test.')
    parser.add_argument('--plot', dest='plot', action='store_true')
    parser.set_defaults(feature=False)
    return parser.parse_args()
