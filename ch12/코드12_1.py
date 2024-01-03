def sortGapInsertion(A, first, last, gap) :
    for i in range(first+gap, last+1, gap) :
        key = A[i]
        j = i - gap
        while j >= first and key<A[j] :
            A[j + gap] = A[j]
            j = j - gap
        A[j + gap] = key

