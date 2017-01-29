# This is a default dictionary based approach

from collections import defaultdict

def finder(arr1,arr2):
    
    d = defaultdict(int)
    
    for num in arr1:
        d[num] += 1
        
    for num in arr2:
        d[num] -= 1

    for i in d.iterkeys():
        if d[i] != 0:
            print i
