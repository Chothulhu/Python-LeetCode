def mergeSort(A):
    mergeSort2(A, 0, len(A)-1)

def mergeSort2(A, first, last):
    if first < last:
        middle = (first + last) // 2
        mergeSort2(A, first, middle)
        mergeSort2(A, middle+1, last)
        merge(A, first, middle, last)

def merge(A, first, middle, last):
    L = A[first:middle+1]
    R = A[middle+1:last+1]
    L.append(999999999)
    R.append(999999999)
    i = j = 0

    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

A = [2, 6, 2, 7, 2, 7, 8, 3, 9, 2, 6, 6, 3, 74, 23, 326, 236, 125]
print(A)
mergeSort(A)
print(A)