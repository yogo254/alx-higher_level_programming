#!/usr/bin/python3


if __name__ == '__main__':
    import sys
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print('0 arguments.')
    elif num_args == 1:
        print('{:d} argument:'.format(num_args))
    else:
        print('{:d} arguments:'.format(num_args))

    for i in range(1, num_args+1):
        print('{:d}: {:s}'.format(i, sys.argv[i]))
