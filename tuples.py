# Just Terry playing around with tuples...

tuple1 = (0, 1, 2, 3)
tuple2 = 0, 1, 2, 3 

print(tuple1)
print(tuple2)

list1 = [1, 2, 3, 4, 5, 6]
list1.append(7)
print(list1)
list1.pop()
print(list1)

#swapping variables with tuples to avoid the usage of temporary variable

#traditional approach
temp = a 
a = b 
b = temp 

#tuple approach
(a, b) = (b, a)
