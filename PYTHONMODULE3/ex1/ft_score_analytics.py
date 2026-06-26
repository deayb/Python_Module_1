#! /usr/bin/env python3

import sys


def main() -> None:
    print('=== Player Score Analytics ===')
    if len(sys.argv) == 1:
        print('No scores provided. Usage: python3 '
              'ft_score_analytics.py <score1> <score2> ...')
    else:
        invalid = [val for val in sys.argv[1:]
                   if not val.lstrip('-').isdigit()]
        if invalid:
            for val in invalid:
                print(f'Invalid parameter: {val}')
            print('No scores provided. Usage: python3 '
                  'ft_score_analytics.py <score1> <score2> ...')
        else:
            args = [int(argv) for argv in sys.argv[1:]]
            average = sum(args) / len(args)
            print(f'Scores processed: {args}')
            print(f'Total players: {len(args)}')
            print(f'Total score: {sum(args)}')
            print(f'Average score: {average}')
            print(f'High score: {max(args)}')
            print(f'Low score: {min(args)}')
            print(f'Score range: {max(args) - min(args)}')


if __name__ == '__main__':
    main()
