import numpy as np

mylist = [1,2,3]
print(type(mylist))

myarray = np.array(mylist)  #converting a python list to a numpy array
print(type(myarray))

print(np.arange(0,10,4))  

print(np.zeros(shape=(3,3))) #creates an array of the specified shape filled with zeroes
#print(np.zeros(shape=(3,3,3))) 
#print(np.ones(shape=(2,2)))

np.random.seed(100)   #ensures same random numbers are generated everytime 
arr = np.random.randint(0,100,10)  
print(arr)

print(arr.argmax(),arr.max())   #index of max element, max element in array 
print(arr.argmin(),arr.min())   

print(arr.mean()) #mean value of elements in array

print(arr.reshape(2,5))  #changing the shape of the array to the required format

#try asking to write a code with whatever they have learnt till now
# (replicate) a function they have learnt to do until now

newmat = arr.copy()
print(newmat)
(newmat.reshape(2,5))[0:1,0:3] = 0
print(newmat)

