def shell_sort(A) :
    n = len(A)
    gap = n//2
    while gap > 0 :
        if (gap % 2) == 0 : gap += 1
        for i in range(gap) :
            sortGapInsertion(A, i, n - 1, gap)
        print('     Gap=', gap, A)
        gap = gap//2