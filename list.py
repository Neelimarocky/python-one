#list
my_list = [10, 20, 30, 40, 50]
print(my_list)
mixed_list = [1, "Hello", 3.14, True]
print(mixed_list)
empty_list = []
print(empty_list)
print(mixed_list[1:5]) 
print(mixed_list[-5:-2])
#adding the elements
my_list = [10, 20, 30]
my_list.append(40)
print(my_list)
my_list.insert(1, 15)
print(my_list)
my_list.extend([50, 60])
print(my_list)
print(len(my_list))
#tuple
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple) 

# A tuple with different data types
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple) 

# A single-element tuple 
single_element_tuple = (10,)
print(single_element_tuple)  # Output: (10,)

# An empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()
print(len(mixed_tuple))
print(mixed_tuple[1:4])
