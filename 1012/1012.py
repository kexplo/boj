# BOJ doesn't support Queue. Why???

#from queue import Queue
from collections import deque
import sys


def find_near_fields(width, height, field):
    ret = []

    x, y = field
    if x - 1 >= 0:
        ret.append((x-1, y))
    if y - 1 >= 0:
        ret.append((x, y-1))
    if x + 1 < width:
        ret.append((x+1, y))
    if y + 1 < height:
        ret.append((x, y+1))
    return ret


def calculate_min_worms(width, height, cabbages):
    def has_cabbage_filter(field):
        return field in cabbages

    # remain_fields_queue = Queue()
    remain_fields_queue = deque()
    for cabbage in cabbages:
        # remain_fields_queue.put(cabbage)
        remain_fields_queue.append(cabbage)

    visitied = set()
    count_worms = 0
    # while not remain_fields_queue.empty():
    while len(remain_fields_queue) > 0:
        # field = remain_fields_queue.get()
        field = remain_fields_queue.pop()
        if field in visitied:
            continue
        count_worms += 1
        # q = Queue()
        # q.put(field)
        q = deque()
        q.append(field)
        # while not q.empty():
        while len(q) > 0:
            # f = q.get()
            f = q.pop()
            for near_field in filter(has_cabbage_filter,
                                     find_near_fields(width, height, f)):
                if near_field in visitied:
                    continue
                # q.put(near_field)
                q.append(near_field)
                visitied.add(near_field)
    return count_worms


def line_gen(lines):
    for line in lines:
        yield line.strip()


def main(lines):
    line_iterator = line_gen(lines)
    num_testcases = int(next(line_iterator))
    for i in range(num_testcases):
        # cabbages
        metadata = next(line_iterator)
        width, height, num_cabbages = map(int, metadata.split(' '))
        lines = [next(line_iterator) for n in range(num_cabbages)]
        cabbages = [tuple(map(int, l.split(' '))) for l in lines]
        print(calculate_min_worms(width, height, cabbages))

main(sys.stdin.readlines())
