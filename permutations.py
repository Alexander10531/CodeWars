from itertools import permutations as per
from collections import Counter

def permutations(string):
    string = list(per(string))
    return list(set(["".join(i) for i in string]))


