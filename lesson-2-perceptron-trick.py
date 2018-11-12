import numpy as np

linear_params = np.array([3, 4, -10])
point = np.array([1, 1, 1])
learning_rate = 0.1
solution = np.dot(linear_params, point)
application_count = 0
while solution != 0:
    application_count += 1
    new_linear_params = np.add(linear_params, learning_rate*application_count)
    solution = np.dot(new_linear_params, point)
print(application_count)
