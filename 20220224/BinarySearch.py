import time


def binarySearch(arr, low, high, x):

    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)

        else:
            return binarySearch(arr, mid + 1, high, x)

    else:
        return -1


def main(arr, query):
    startTime = time.time()
    ans = binarySearch(arr, 0, len(arr)-1, query)

    if ans != -1:
        print("Value Found at index:", ans, end="\t")
    else:
        print("This element cannot be found!", end="\t")

    print("For Array Size:", len(arr), ", Query:", query,
          ", Time Taken: ", time.time()-startTime, "seconds")
