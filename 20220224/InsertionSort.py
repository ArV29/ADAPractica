import time


def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def main(arr):
    arrCpy = arr.copy()
    n = len(arrCpy)
    startTime = time.time()
    insertionSort(arrCpy)

    print("Sorted Array of length", n, "in", time.time()-startTime, "seconds")
