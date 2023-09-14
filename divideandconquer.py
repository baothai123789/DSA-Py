
def findmaxcrossarray(arr, low, mid, hight):
    leftsum = 0
    maxleftsum = -1000
    for i in range(mid, low - 1, -1):
        leftsum += arr[i]
        maxleftsum = max(maxleftsum, leftsum)
    rightsum = 0
    maxrightsum = -1000
    for j in range(mid + 1, hight + 1):
        rightsum += arr[j]
        maxrightsum = max(maxrightsum, rightsum)
    return max(maxrightsum, maxleftsum, maxrightsum + maxleftsum)

Print



