from random import randint
from time import time
from quicksort_logarithm import quicksort
def genArray(size, nSize = 10):
    return [randint(0, nSize) for i in range(0, size)]
#print(testArray)
n = 10
while True:
    testArray = genArray(n)
    start = time()
    quicksort(testArray)
    print(n, time() - start, sep="\t")
    n *= 10
#print(testArray)
