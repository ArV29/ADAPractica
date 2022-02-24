from numpy import random
import time
import MergeSort
import QuickSort
import LinearSearch
import BinarySearch
random.seed(100)
arrays = [random.randint(1, 80, size=(40)),random.randint(1, 800, size=(400)),random.randint(1, 8000, size=(4000)),random.randint(1, 80000, size=(40000))]

print("SORTING using MERGE SORT")
for array in arrays:
  MergeSort.main(array)
  
print("SORTING using QUICK SORT")
for array in arrays:
  QuickSort.main(array)

for array in arrays:
  array.sort()

print("SEARCHING using LINEAR SEARCH")

queries = [60, 600, 6000, 60000]

for i, query in enumerate(queries):
  LinearSearch.main(arrays[i], query)

print("SEARCHING using BINARY SEARCH")


for i, query in enumerate(queries):
  BinarySearch.main(arrays[i], query)
