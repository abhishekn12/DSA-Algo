"""
2
6
0 1 2 2 1 0
7
0 1 2 1 2 1 2

Sample Output 1 :
0 0 1 1 2 2
0 1 1 1 2 2 2
"""

def sort012(arr, n) :
    
    lo = 0
    hi = len(arr) - 1
    mid = 0
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo = lo + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi = hi - 1
    return arr
    pass