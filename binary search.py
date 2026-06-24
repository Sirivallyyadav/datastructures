def binary_search(ls,target):
    low=0
    high = len(ls)-1
    while low <= high:
        mid = (low+high)//2
        if ls[mid] == target:
            return mid
        elif ls[mid]<target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
ls=[11,2,3,41,5,6,7,8,92]
print(binary_search(ls,8))
