#!/usr/bin/env python

import argparse
import sys

from go import Game


def main():
    parser = argparse.ArgumentParser(description='Starts a game of go in the terminal.')
    parser.add_argument('-s', '--size', type=int, default=19, help='size of board')

    args = parser.parse_args()

    if args.size < 7 or args.size > 19:
        sys.stdout.write('Board size must be between 7 and 19!\n')
        sys.exit(0)
    game = Game()
    game.run(args.size)


if __name__ == '__main__':
    main()
