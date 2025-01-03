# Example 1: operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)
    def __str__(self):
        return f"Vector: ({self.x}, {self.y})"
# Example 2: Using operator overloading for vector addition
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(3, 4)
v4 = Vector(3, 4)
result_vector = v1 + v2
print(result_vector)
# Example 1: Operator Overloading
class Vector:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
    def __add__(self, *others):
        sum_vector = Vector(self.x , self.y)
        for other in others:
            sum_vector = Vector(sum_vector.x + other.x, sum_vector.y + other.y)
        return sum_vector
    def __sub__(self, *others):
        sub_vector = Vector(self.x , self.y)
        for other in others:
            sub_vector = Vector(sub_vector.x - other.x, sub_vector.y - other.y)
        return sub_vector
    def __mul__(self, *others):
        mul_vector = Vector(self.x , self.y)
        for other in others:
            mul_vector = Vector(mul_vector.x * other, mul_vector.y * other)
        return mul_vector
    def __str__(self):
        return f"vector: ({self.x}, {self.y})"
# Exapmle 2: Using operator overloading for vector addition
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(3, 4)
v4 = Vector(3, 4)
result_vector = v1 + v2+v3+v4
print(result_vector)
# Example 5: Exceptions
# Example 5.1: Handling division by zero
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Exception:",e) # Output: Exception: division by zero
# Exapmle 5.2: Handling index out of range
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print("Exception:", e) # Output: Exception: list index out of range