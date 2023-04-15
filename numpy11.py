#numpy--->numerical python ----> core library for numeric and scientific calculations
# consists of multidimensional array object and a collection of routines /methods/functions for process
#numpy array has homogenous elements


import numpy as np
#single dimensional array
n1=np.array([1,2,3,4,5,6])
print(n1)
print(type(n1))



#multidimentional array
n2=np.array(([1,2,3,4,5],[6,7,8,9,10]))
print(n2)
#initialize with zero
n3=np.zeros((3,3))
print(n3)


n4=np.zeros((5,5))
print("\n")
print(n4)

n5=np.full((4,3),20)#same value will be 
print(n5)




n6=np.arange(10,30)
print(n6)
print(n6.dtype)
print(n6.itemsize)


arr6=np.linspace(1,10,3)
print(arr6)


arr7=np.empty(2,3)
print(arr7)

arr8=np.empty_like(arr6)
print(arr8)

