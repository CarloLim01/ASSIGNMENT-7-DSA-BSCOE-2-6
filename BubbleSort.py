# BUBBLE SORT

def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                
                print(nums)

nums = [59, 61, 81, 11, 47, 63, 9, 6, 48, 35]
print("BUBBLE SORT")
print("Array Values: [59, 61, 81, 11, 47, 63, 9, 6, 48, 35]\n")
print("Process: ")
bubble_sort(nums)
print('\t')
print(f'Sorted array: {nums}')