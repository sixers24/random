from itertools import combinations
import itertools



def get_pairs(array):
    return [ (i[0], i[1]) for i in combinations(array, 2)]
    