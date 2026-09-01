#! /usr/bin/env python3

import sys


def main() -> None:
    print('=== Command Quest ===')
    print(f'Program name: {sys.argv[0]}')
    lenn = len(sys.argv)
    if (len(sys.argv) == 1):
        print('No arguments provided!')
    else:
        print(f'Arguments received: {lenn - 1}')
        for index, valeur in enumerate(sys.argv[1:]):
            print(f'Argument {index + 1}: {valeur}')
    print(f'Total arguments: {lenn}')


if __name__ == '__main__':
    main()
