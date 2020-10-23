def findValueSortedShiftedArray(nums, target):
    min_idx = 0
    max_idx = len(nums) + 1

    while min_idx < max_idx:
        mid_idx = (min_idx + max_idx) // 2
        
        if target  == nums[mid_idx]:
            return mid_idx
            
        elif nums[mid_idx] < target:
            min_idx = mid_idx + 1

        else: 
            max_idx = mid_idx - 1


    return -1