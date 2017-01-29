def pair_sum(lst,k):
    
    if len(lst) < 2:
        print "Can form a pair if there are at least two elements"
        return
    
    # Make two sets for tracking purpose
    seen = set()
    output = set()
    
    # Set target as difference between k and num and if target is not in seen add it else add to output the (num,target) pair.
    for num in lst:
        target = k - num
            
        if target not in seen:
            seen.add(num)
                
        else:
            output.add((min(num,target),max(num,target)))
    
    # Print the result
    print "Total of " + str(len(output)) +" pairs found, they are as follows :"
    for i in output:
        print i
