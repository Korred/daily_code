from collections import defaultdict


def same_necklace(n1, n2):
    if len(n1) != len(n2):
        return False

    if n1 == n2:
        return True

    n1 = list(n1)
    n2 = list(n2)

    for i in range(len(n1) - 1):
        n1.append(n1.pop(0))
        if n1 == n2:
            return True

    return False


def repeats(n):
    cnt = 1
    n = list(n)

    # necklace copy
    nc = n[:]

    for i in range(len(nc) - 1):
        nc.append(nc.pop(0))
        if nc == n:
            cnt += 1

    return cnt


def find_same_necklace_in_file(file_name):

    necklace_set = set()

    with open(file_name, "r") as f:
        for line in f:
            n = tuple(line.strip())
            necklace_set.add(n)

    found_list = list()

    while necklace_set:
        found = set()

        # returns random element
        org = list(necklace_set.pop())
        cop = org[:]

        for i in range(len(cop) - 1):
            cop.append(cop.pop(0))
            if tuple(cop) in necklace_set:
                found.add(tuple(org))
                found.add(tuple(cop))

                necklace_set.remove(tuple(cop))

        if found:
            found_list.append(["".join(n) for n in found])

    # print(found_list)

    for n in found_list:
        if len(n) == 4:
            print(n)


find_same_necklace_in_file("enable1.txt")
