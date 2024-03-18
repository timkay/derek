from random import randint
from time import time
import quicksort_logarithm as quicksort
def genArray(size, nSize = 10):
    return [randint(0, nSize) for i in range(0, size)]
#print(testArray)
try:
    n = 10
    while True:
        testArray = genArray(n)
        amount = sum(testArray)
        start = time()
        quicksort.quicksort(testArray)
        assert sum(testArray) == amount
        for i in range(1, len(testArray) - 1):
            assert testArray[i - 1] <= testArray[i]
        print(n, time() - start, quicksort.maxdepth, sep="\t")
        n *= 10
except KeyboardInterrupt:
    print("Ctrl-C")
#print(testArray)
