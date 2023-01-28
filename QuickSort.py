# QUICK SORT

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)
        
def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    
    return end

if __name__ == '__main__':
    elements = [59, 61, 81, 11, 47, 63, 9, 6, 48, 35]
    print("QUICK SORT\n")
    print("Array Values: [59, 61, 81, 11, 47, 63, 9, 6, 48, 35]\n")
    quick_sort(elements, 0, len(elements)-1)
    print(f'Sorted array: {elements}')