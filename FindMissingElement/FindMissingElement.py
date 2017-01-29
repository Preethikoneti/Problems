def finder(arr1,arr2):
    
    # Sort both the arrays
    arr1.sort()
    arr2.sort()
    
    # Create an empty list
    ot = []
    
    # To check when the mismatch starts
    for i in range(min(len(arr1),len(arr2))):
        ot.append(arr1[i] == arr2[i])
    
    # Print the first mismatched value in arr1, since both are sorted array
    for i in ot:
        if i == False:
            print arr1[ot.index(i)]
            break
