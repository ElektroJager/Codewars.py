def first_non_consecutive(arr):
    if len(arr) == 1:
        return arr[0]
    #your code here
    iterator = arr.pop(0)
    for nmbr in arr:
        iterator += 1
        if (nmbr != iterator):
            print(nmbr)
            return nmbr

    return None

arr = [1,2,3,5,6]
first_non_consecutive(arr)
