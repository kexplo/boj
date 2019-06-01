# -*- coding: utf-8 -*-

import sys


def box(level):
    if level == 0:
        return '*'
    block = box(level-1)
    block_size = 3 ** (level-1)
    box_lines = []
    for line in block.split('\n'):
        box_lines.append(line * 3)
    for line in block.split('\n'):
        box_lines.append(line + (' ' * block_size) + line)
    for line in block.split('\n'):
        box_lines.append(line * 3)
    return '\n'.join(box_lines)


def logint(value, base):
    log = 0
    while value > 1:
        value = value // base
        log += 1
    return log


def main(number):
    exponent = logint(number, 3)
    lines = box(exponent)
    print(box(exponent))
    assert len(lines.split('\n')) == number



def test():
    for i in range(1, 9):
        print('test: 3 ** {}, {}'.format(i, 3 ** i))
        main(3 ** i)
test()
# main(int(sys.stdin.readline().strip()))
