def binaryserch(arr, target, recur=None):
    if recur:
        def bsearchrecur(arr, target, l, h):
            if l <= h:
                mid = (l+h)//2
                if arr[mid] == target:
                    return mid
                if arr[mid] > target:
                    bsearchrecur(arr, target, l, mid-1)
                else:
                    bsearchrecur(arr, target, mid+1, h)
            else:
                return -1
        return bsearchrecur(arr, target, 0, len(arr)-1)
    i = 0
    j = len(arr)-1
    while i <= j:
        mid = (i+j)//2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            i = mid+1
        else:
            j = mid-1
    return -1

