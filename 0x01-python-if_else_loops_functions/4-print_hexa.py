#!/usr/bin/python3
def get_hexa(number):
    hexString = '0123456789abcdef'
    tens = number // 16
    ones = number % 16
    if tens > 0:
        return hexString[tens] + hexString[ones]
    else:
        return hexString[ones]


if __name__ == '__main__':
    for number in range(99):
        print('{:d} = 0x{}'.format(number, get_hexa(number)))
