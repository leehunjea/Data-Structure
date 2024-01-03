def partition(A, left, right) :
	low = left + 1
	high = right
	pivot = A[left]
	while (low < high) :
	    while low <= right and A[low] < pivot : low += 1
	    while high >= left and A[high]> pivot : high-= 1

	    if low < high :
	        A[low], A[high] = A[high], A[low]

	A[left], A[high] = A[high], A[left]
	return high
