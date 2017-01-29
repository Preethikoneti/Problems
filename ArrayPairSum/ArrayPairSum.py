# import itertools so we can generate all possible pairs from the given list

import itertools

def pair_sum(lst,k):
    
    if len(lst) < 2:
        print "Can form a pair if there are at least two elements"
    
    # Generate all possible pairs, note that (1,2) is same as (2,1)
    lop = list(itertools.combinations(lst, 2))
    
    # Check if the sum of pair is k
    lop_m = [(i,j) for i,j in lop  if i + j == k]
    
    # Output those pairs
    print "Total of " + str(len(lop_m)) + " Pairs found, they are as follows:"
    for i in lop_m:
        print i
