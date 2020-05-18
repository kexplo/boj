from collections import defaultdict
import sys

def read_peoples(input_line):
    num, _, remain = input_line.strip().partition(' ')
    if int(num) == 0:
        return 0, []
    return int(num), [int(x) for x in remain.split(' ')]


parties_by_people = defaultdict(set)
peoples_by_party = {}


def main(input_lines):
    num_peoples, num_parties = [int(x)
                                for x in input_lines[0].strip().split(' ')]
    num_truths, truth_peoples = read_peoples(input_lines[1])

    truth_parties = set()

    i = 0
    while i < num_parties:
        _, party_peoples = read_peoples(input_lines[2+i])
        peoples_by_party[i] = party_peoples
        for pp in party_peoples:
            parties_by_people[pp].add(i)
            if pp in truth_peoples:
                truth_parties.add(i)
        i += 1

    tpp = set()
    visited_parties = set()
    def mark_truth_party(party_idx):
        if party_idx in visited_parties:
            return
        visited_parties.add(party_idx)
        for tp in peoples_by_party[party_idx]:
            for pbp in parties_by_people[tp]:
                mark_truth_party(pbp)
        tpp.add(party_idx)

    for truth_party in truth_parties:
        mark_truth_party(truth_party)

    print(num_parties - len(tpp))


main(sys.stdin.readlines())
