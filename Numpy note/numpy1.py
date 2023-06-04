import numpy as np

#a = np.random.randint(0, 10, 3) #from 0 to 9, 3 numbers
#print(a)
#print()

#b = np.random.randint(0, 10, (3, 4)) #from 0 to 9, a 4*3 area
#print(b)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
print()

np.random.shuffle(arr)
print(arr)