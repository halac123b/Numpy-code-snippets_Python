import numpy as np

tuple_sample = (1, 2, 3)

# Convert tuple to Numpy array
# in: tuple, data type
# array([1.0, 2.0, 3.0])
as_array = np.asarray(tuple_sample, dtype=np.float64)

# Tạo 1 Numpy array với mỗi gt bằng as_array
# in: shape, (200, 200, 3): mảng 3 chiều với kích thước 200x200x3
##### fill_value: trong mảng 200x200, mỗi item chứa 3 giá trị tương ứng với as_array
shape = np.full(shape=(200, 200, 3), fill_value=as_array, dtype=np.uint8)
# Thay vì full() với shape tự xác định, ta dùng full_like() với shape đã có sẵn
same_shape = np.full_like(a=shape, fill_value=as_array, dtype=np.uint8)

# Get data type of Numpy array
print(same_shape.dtype)
