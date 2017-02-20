def MissingInteger_Total(lst,Range):
    """
    This method takes an list of n-1 integers and given range of 1 to n and prints out the missing integer using Total sum method.
    """
    
    n = len(Range)
    
    # Compute the total sum of n integers
    total = (n*(n+1))/2
    
    # Subtract elements of input list from total, reslutant total is the missing integer
    for i in lst:
        total -= i
    
    return int(total)
