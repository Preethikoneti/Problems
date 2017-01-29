# import itertools so we can generate all possible pairs from the given list

import itertools

def pair_sum(lst,k):
    
    # Generate all possible pairs, note that (1,2) is same as (2,1)
    lop = list(itertools.combinations(lst, 2))
    
    # Check if the sum of pair is k
    lop_m = [(i,j) if i + j == k else False for i,j in lop]
    
    # Output those pairs
    for i in lop_m:
        if not i == False:
            print i
