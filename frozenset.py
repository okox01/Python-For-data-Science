# Creating a frozenset with elements 1, 2, 3, 4, and 5
fs = frozenset([1, 2, 3, 4, 5])  

# Printing the frozenset (output: frozenset({1, 2, 3, 4, 5}))
print(fs)  

# Trying to add an element to the frozenset (this will cause an error)
fs.add(5)  # ❌ AttributeError: 'frozenset' object has no attribute 'add'

# Trying to remove an element from the frozenset (this will also cause an error)
fs.remove(1)  # ❌ AttributeError: 'frozenset' object has no attribute 'remove'



# Creating two frozensets
A = frozenset([1, 2, 3, 4, 5])  
B = frozenset([2, 4, 7, 6, 3])  

# Union of A and B (combines all unique elements from both sets)
print(f"Union of sets: {A | B}")  
# Output: frozenset({1, 2, 3, 4, 5, 6, 7})

# Intersection of A and B (common elements in both sets)
print(f"Intersection of sets: {A & B}")  
# Output: frozenset({2, 3, 4})

# Difference (elements in A but not in B)
print(f"Difference between sets: {A - B}")  
# Output: frozenset({1, 5})

# Symmetric Difference (elements in either A or B, but not both)
print(f"Symmetric Difference of sets: {A ^ B}")  
# Output: frozenset({1, 5, 6, 7})



# Defining two sets
s1 = {1, 5, 6, 8}  
s2 = {2, 5, 1, 9, 10}  

# Union (combines all unique elements from both sets)
print(s1 | s2)  
# Output: {1, 2, 5, 6, 8, 9, 10}

# Intersection (common elements in both sets)
print(s1 & s2)  
# Output: {1, 5}

# Difference (elements in s1 but not in s2)
print(s1 - s2)  
# Output: {6, 8}

# Symmetric Difference (elements in either set, but not both)
print(s1 ^ s2)  
# Output: {2, 6, 8, 9, 10}

