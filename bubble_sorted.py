def bubble_sort(nums):
    n = len(nums)
    counter = 0
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                counter += 1
    print(scores)
    print(counter)
scores = [45, 12, 89, 33, 67, 21, 90, 5]
bubble_sort(scores)