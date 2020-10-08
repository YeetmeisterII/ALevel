import numpy as np

x = 4
y = 4
x1 = np.full((1, 1, 3), 255)
print(f"x1 {x1}")

x2 = np.array([0, 1, 3, 4]).reshape(4)
print(f"x2 {x2}")

x3 = np.multiply(x2, x1)
print(f"x3 {x3}")
print(f"x3[0][0] {x3[0][0]}")
# print(x2)
