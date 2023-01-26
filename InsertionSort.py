# INSERTION SORT

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor
        
        print(elements)

if __name__ == '__main__':
    elements = [59, 61, 81, 11, 47, 63, 9, 6, 48, 35]
    print("INSERTION SORT\n")
    print("Array Values: [59, 61, 81, 11, 47, 63, 9, 6, 48, 35]\n")
    print("Process: ")
    insertion_sort(elements)
    print('\t')
    print(f'Sorted array: {elements}')