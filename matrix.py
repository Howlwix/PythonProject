import numpy as np
arr = np.random.randint(0 , 101,(4,4))
arr[arr <= 60] = 0
arr =arr+5
row_1 = arr[0,:]
row_2 = arr[1,:]
row_3 = arr[2,:]
row_4 = arr[3,:]
mean_arr = np.mean(arr)
max_arr = np.max(arr)
mean_row_1 = np.mean(row_1)
mean_row_2 = np.mean(row_2)
mean_row_3 = np.mean(row_3)
mean_row_4 = np.mean(row_4)
print(mean_arr)
print(max_arr)
print(mean_row_1)
print(mean_row_2)
print(mean_row_3)
print(mean_row_4)

