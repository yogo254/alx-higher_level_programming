#!/usr/bin/python3
def printNumberCombinations():
    for x in range(10):
        for y in range(x + 1, 10):
            if x == 8 and y == 9:
                print('{:d}{:d}'.format(x, y))
            else:
                print('{:d}{:d}'.format(x, y), end=', ')


if __name__ == '__main__':
    printNumberCombinations()
