from collections import defaultdict
import sys

def is_can_eat(eater_shark, shark):
    return eater_shark[0] >= shark[0] and \
        eater_shark[1] >= shark[1] and \
        eater_shark[2] >= shark[2]


def main(input_lines):
    count = int(input_lines[0].strip())
    sharks = []
    for i in range(1, count+1):
        abils = [int(x) for x in input_lines[i].strip().split(' ')]
        sharks.append(abils)
    sharks = sorted(sharks, key=lambda x: sum(x), reverse=True)

    eat_candidates = defaultdict(set)
    i = 0
    while i < count-1:
        j = i+1
        while j < count:
            if is_can_eat(sharks[i], sharks[j]):
                eat_candidates[i].add(j)
            elif is_can_eat(sharks[j], sharks[i]):
                eat_candidates[j].add(i)
            j += 1
        i += 1

    eaten_by = {}
    visited_candidate = set()

    def find_candidate(eater_idx):
        for candidate in eat_candidates[eater_idx]:
            if candidate in visited_candidate:
                continue
            visited_candidate.add(candidate)
            if candidate not in eaten_by or find_candidate(eaten_by[candidate]):
                eaten_by[candidate] = eater_idx
                return True
        return False

    for eater_idx in eat_candidates.keys():
        find_candidate(eater_idx)
        visited_candidate.clear()  # reset visited marks
        find_candidate(eater_idx)  # eat twice
    print(count - len(eaten_by))


main(sys.stdin.readlines())
