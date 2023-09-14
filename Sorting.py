def insertion_sort(arr: list):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j > 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


def buble_sort(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        minidx = i
        for j in range(i + 1, n):
            if arr[j] < arr[minidx]:
                minidx = j
        if minidx != i:
            arr[i], arr[minidx] = arr[minidx], arr[i]


def merg_sort(arr, *, itermethod=False):
    def merg(arr, start, mid, end):
        L = arr[start:mid + 1]
        R = arr[mid + 1:end + 1]
        i, j, k = 0, 0, start
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1

    def mergsort(arr, start, end):
        if end - start > 0:
            mid = (start + end) // 2
            mergsort(arr, start, mid)
            mergsort(arr, mid + 1, end)
            merg(arr, start, mid, end)

    mergsort(arr, 0, len(arr))


def heap_sort(arr):
    def down_heap(data, i, n):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        largest = left if left < n and data[left] > data[largest] else largest
        largest = right if right < n and data[right] > data[largest] else largest
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            down_heap(data, largest, n)

    n = len(arr)
    for i in range((n - 1) // 2, -1, -1):
        down_heap(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        down_heap(arr, 0, i)


def quick_sort(arr):
    def partition(data, left, right):
        pivot = right
        i = left 
        for j in range(left,right):
            if arr[j] <= arr[pivot]:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
        arr[i], arr[pivot] = arr[pivot], arr[i]
        return i
            
    def qsort(data, left, right):
        if left < right:
            j = partition(data, left, right)
            qsort(data, left, j - 1)
            qsort(data, j + 1, right)

    qsort(arr, 0, len(arr) - 1)
    
