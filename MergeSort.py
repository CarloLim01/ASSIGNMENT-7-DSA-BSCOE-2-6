# MERGE SORT

def merge_sort(elements):
    if len(elements) <= 1:
        return

    mid = len(elements)//2

    left = elements[:mid]
    right = elements[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, elements)
    print(elements)

def merge_two_sorted_lists(a,b,elements):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            elements[k] = a[i]
            i+=1
        else:
            elements[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        elements[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        elements[k] = b[j]
        j+=1
        k+=1
        
    print(elements)

if __name__ == '__main__':
    elements = [59, 61, 81, 11, 47, 63, 9, 6, 48, 35]
    print("MERGE SORT\n")
    print("Array Values: [59, 61, 81, 11, 47, 63, 9, 6, 48, 35]\n")
    print("Process: ")
    merge_sort(elements)
    print('\t')
    print(f'Sorted array: {elements}')