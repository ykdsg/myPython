import numpy as np

t1: np.ndarray = np.arange(12).reshape(3, 4).astype("float")
print(t1)
print("*" * 100)
t1[1, 2:] = np.nan

print(t1)
print("&" * 100)

# print(t1.shape[1])
# 遍历每一列
for i in range(t1.shape[1]):
    temp_col = t1[:, i]
    # nan !=nan
    nan_num = np.count_nonzero(temp_col != temp_col)
    # 不为0，说明这一列有nan
    if nan_num != 0:
        # 当前这列不为nan 的array
        temp_not_nan_col: np.ndarray = temp_col[temp_col == temp_col]
        # print(temp_not_nan_col)
        # print("*" * 100)
        not_nan_mean_col = temp_not_nan_col.mean()
        temp_col[temp_col != temp_col] = not_nan_mean_col

print(t1)
