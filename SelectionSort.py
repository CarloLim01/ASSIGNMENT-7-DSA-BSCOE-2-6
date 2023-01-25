# SELECTION SORT

def selection_sort(nums):
    for i in range(9):
        minpos = i
        for j in range(i,10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)
        
nums = [59, 61, 81, 11, 47, 63, 9, 6, 48, 35]
print("SELECTION SORT")
print("Array Values: [59, 61, 81, 11, 47, 63, 9, 6, 48, 35]\n")
print("Process: ")
selection_sort(nums)
print('\t')
print(f'Sorted array: {nums}')