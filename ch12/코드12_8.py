def quick_sort(A, left, right) :
	if left<right :
		q = partition(A, left, right)
		quick_sort(A, left, q - 1)
		quick_sort(A, q + 1, right)
