def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    first=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=first
    return arr
