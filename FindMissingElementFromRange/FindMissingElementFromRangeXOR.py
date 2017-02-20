def MissingInteger_XOR(lst,Range):
    """
    This method takes an input list of n-1 integers and given range of 1 to n and prints out the missing integer.
    """
    
    # Perform the XOR between two lists after converting them into sets, this will leave only missing integer,
    # As A XOR A is 0.
    # Converted to list since sets in python doesn't support indexing.

    return list(set(sorted(lst)) ^ set(sorted(Range)))[0]
