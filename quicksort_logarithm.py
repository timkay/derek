maxdepth = 0
def quicksort(array, bottom = 0, top = None, depth = 0):
        global maxdepth
        if maxdepth < depth: maxdepth = depth
        if top == None:
                top = len(array) - 1
        if bottom >= top or bottom < 0 or all(i == array[top] for i in array[bottom:top]): 
                return
        p = _partition(array, bottom, top) 
        try:
                quicksort(array, bottom, p - 1, depth + 1)
                quicksort(array, p + 1, top, depth + 1)
        except RecursionError:
                pass

def _partition(array, bottom, top):
        pivot = array[top]
        i = bottom - 1
        for j in range(bottom, top):
                if array[j] <= pivot: 
                        i += 1
                        array[i], array[j] = array[j], array[i]
        i += 1
        array[i], array[top] = array[top], array[i]
        return i
