def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    print(nums)
    print(f"highest score : {max(nums)}")
    print(f"lowest score : {min(nums)}")

scores = [100, 90, 78, 67, 55, 45, 23, 12]
selection_sort(scores)

