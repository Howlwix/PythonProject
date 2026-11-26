def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    print(nums)
    highest_score = nums[0]
    for num in nums:
        if num > highest_score:
            highest_score = nums[i]
    print(f'highest_score : {highest_score}')
    lowest_score = nums[0]
    for num in nums:
        if num < lowest_score:
            lowest_score = num
    print(f'lowest_score : {lowest_score}')

scores = [100, 90, 78, 67, 55, 45, 23, 12]
selection_sort(scores)

