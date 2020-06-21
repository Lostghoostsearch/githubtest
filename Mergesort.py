def merge(array1,array2):
    array3 = []
    while len(array1)!=0 and len(array2)!=0:
        if array1[0]>array2[0]:
            array3.append(array2[0])
            array2.remove(array2[0])
        else:
            array3.append(array1[0])
            array1.remove(array1[0])

    while len(array1)!= 0:
        array3.append(array1[0])
        array1.remove(array1[0])

    while len(array2) != 0:
        array3.append(array2[0])
        array2.remove(array2[0])

    return array3

def merge_sort(sequence):
    n = len(sequence)
    if n<=1:
        return sequence
    elif n==2:
        A = [sequence[0]]
        B = [sequence[1]]
        arrayA = merge_sort(A)
        arrayB = merge_sort(B)
        return merge(arrayA,arrayB)
    else:
        BI =0
        EI = n-1
        MPI = BI +((EI-BI)//2)
        A = sequence[:MPI]
        B = sequence[MPI:]
        arrayA = merge_sort(A)
        arrayB = merge_sort(B)
        return merge(arrayA,arrayB)

        
sort = merge_sort([2,1])    
   
        

        
