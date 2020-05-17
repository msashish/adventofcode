#!/usr/bin/env python3

import os
import sys
import argparse

# from typing import List

#print(sys.path)
#print(os.getenv('PYTHONPATH'))


# def parse_args(args: List[str]) -> argparse.Namespace:
def parse_args(args):
    parser = argparse.ArgumentParser(description='Sample testing')

    parser.add_argument('--name', dest='name', required=True, help='your name, thats all')
    parser.add_argument('--message', dest='msg', default='',
                        required=False, help='give some message if you like')

    return parser.parse_args(args=args)


def main(args_passed):
    print("sample.py started")
    print("Reassigning pid " + str(os.getpid()) + " to sample.py")

    args = parse_args(args_passed)
    print("Argument passed = ", args.name, args.msg)
    print('Env xyz_env = ' + os.getenv('xyz_env', ''))
    print('Env myname_env = ' + os.getenv('myname_env', ''))


if __name__ == '__main__':
    main(sys.argv[1:])
