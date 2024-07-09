import numpy as np

# input array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# stack() is used for joining multiple NumPy arrays.
## it joins arrays along a new axis. It returns a NumPy array.
## 2 array phải có cùng hình dạng (a x b..)
## Tạo array mới nhiều hơn 2 input 1 chiều (stack 2 array 1 chiều → 2 chiều)
## axis: chiều của stack

# axis=n: vd ban đầu array có shape (a, b)
## kết quả chèn 2 vào shape tùy vào index của n
## n = 0: (2, a, b), n = -1: (a, b, 2)
c = np.stack((a, b), axis=0)
print(c)
