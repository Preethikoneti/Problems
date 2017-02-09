def MissingInteger_XOR(arr1,arr2):
    """
    This method takes an input list of n-1 integers and given list of n integers and prints out the missing integer in the first list.
    """
    
    # Perform the XOR between two lists after sorting converting them into sets, this will leave only missing integer,
    # As A XOR A is 0.
    # Converted to list since set doesn't support indexing.

    return list(set(sorted(arr1)) ^ set(sorted(arr2)))[0]
