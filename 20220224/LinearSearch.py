import time

from anyio import start_blocking_portal
def search(arr, query):
  for index, value in enumerate(arr):
    if value == query:
      return (True, index)
  return (False, -1)


def main(arr, query):
  startTime = time.time()
  ans = search(arr, query)

  if ans[0]:
    print("Value Found at index: ", ans[1], end="\t")
  else:
    print("This element cannot be found!", end="\t")
  
  print("For Array Size:", len(arr),", Query:",query, ", Time Taken: ", time.time()-startTime, "seconds")


