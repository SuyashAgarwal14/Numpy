
"""
Numpy is used for working with arrays.It provides an array object(called ndarray) that is very fast to process
Numpy is fatser than lists due to their storing in contiguous memor location unlike normal lists
Numpy-multidimensional calculations.represent data in a form and quickly manipulates and perform operations on it
Its is more efficient in memory utilization
Good Cache utilization
"""

import numpy as np

#Basics 
ver=np.__version__                                          #to check numpy version
a=np.array([1,2,3])                                         #array function takes lists, tupple or any array like object and convert it to an ndarray
type_a=type(a)                                              #it tells the type of object passed-numpy.ndarray  for numpy objects
var=a.ndim                                                  #get dimension
var=a.shape                                                 #get shape-shape returns no. of elements in each dimension 
var=a.dtype                                                 #to get datatype
var=a.size                                                  #to get size of an element
var=a.nbytes                                                #to get total size of array in bytes
b=a.T                                                       #transpose an array

#0-D Array-each element in an array
a=np.array(30)

#uni-dimensional or 1-D Array-An array that has 0-D elements as its elements
a=np.array([1,2,3])

#2-D Array-An array that has 1-D arrays as its elements
b=np.array([[4.0,5.0,6.0],[7.0,8.0,9.5]])

#3-D Array-An array that has 2-D arrays as its elements
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

#ndmin specifies the minimum dimensions of resultant array
a=arr = np.array([[1, 2, 3, 4],[5,6,7,8]],ndmin=4)          #returns 4
a=arr = np.array([[1, 2, 3, 4],[5,6,7,8]],ndmin=1)          #return 2
c=np.array([2,4,6],dtype="int32")                           #to specify datatype of the elements in the array.Can use i4 for type

#Accessing/Changing elements, rows and columns
var=b[0,2]                                                  #get specific element
var=b[0,:]                                                  #get specific row
var=b[:,2]                                                  #get specific column
d=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
var=d[0, 1:6:3]                                             #step indexing  [startindex:endindex:stepsize]
d[1,3]=20                                                   #change specific element
d[0,:]=[9,8,7,6,5,4,3]                                      #change row 
d[:,0]=[30,15]                                              #change column
#during changing row and column shape should not be changed

#3-D array
b=np.array([[[1,2],[3,4]],[[4,5],[6,7]]])
var=b[0,1,1]                                                #get specific element (work outside in-from outside to inside)
b[:,1,:]=[[9,8],[7,6]]


#Initializing different types of arrays
a=np.zeros(5,dtype="int16")                                 #vector of length 5
a=np.zeros((2,3))                                           #vector of 2X3
a=np.ones((2,3,4))                                          #3-D array
a=np.full((2,2),99,dtype="float32")                         #for any other number-first argument is shape and second is the number
a=np.random.rand(4,2)                                       #specify shape to get array of random numbers
a=np.random.random_sample(b.shape)                          #gives shape of given variable 
a=np.random.randint(7)                                      #random numbers starting from 0
a=np.random.randint(1,9,size=(3,2))                         #can specify range and size
a=np.identity(7)                                            #makes a identity matrix of given size
arr=np.array([[1,2,3]])
a=np.arange(15)                                             #makes an array of n numbers(0 to n-1).we can reshape it also
a=np.repeat(arr,4,axis=1)                                   #repeats an array arr till some no of times 
#axis=0 means column wise and axis=1 means row wise

c=a.copy()                                                  #to make copy of an array
c=a.view()                                                  #to view array
"""
The Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array, 
and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, 
and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array,
and any changes made to the original array will affect the view.
"""


#Mathematics

#Linear Algebra-numpy allows element wise arithematic operations on the array
a=np.array([1,2,3])
b=np.array([4,5,6])
var=a*2
print(var)
var=a+2
var=a-2
var=a//2
var=a+b
var=a**2
var=np.sin(a)

#Matrix implementation
a=np.ones((2,3))
b=np.full((3,2),2)
c=np.matmul(a,b)                                            #matrix multiplication
var=np.linalg.det(c)                                        #find determinanat
dot_product=np.dot(a,b)                                     #find dot product of two arrays can also be used as a@b
d=np.ones((2,3))
concat=np.concatenate((d,a),axis=1)                         #to concatenate two arrays for multidimensional define axis also
stacking=np.stack((a,d),axis=1)                             #stacking is same as concat but stacking is done along a new axis
v=np.vstack([a,d])                                          #vertically stack the  vectors
h=np.hstack((a,d))                                          #horizontally stack the vectors
d=np.dstack((a,d))                                          #to stack along height same as depth stacking

#Statistics
stats=np.array([[1,2,3],[4,5,6]])
min=np.min(stats)                                           
min_index = np.argmin(stats)                                # returns index of min element in the array
min=np.min(stats,axis=1)                                    #min element on row basis
#max is similar to min

sum=np.sum(stats)
sum=np.sum(stats,axis=1)                                    #row wise sum
sum=np.sum(stats,axis=0)                                    #column wise sum

a=np.array([1,2,3])
b=np.array([4,5,6])
c = a + b
c = np.add(a, b)
# similarlly other mathematical functions like: 
# np.substract() 
# np.negative() -uninary operation 
# np.multiply() 
# np.divide() 
# np.pow() 
# np.mod() 
# np.floor_divide()

#Reorganizing array 
before=np.array([1,2,3,4,5,6])
after=before.reshape(3,2)                                   #reshaping changes number of elements in each dimension.
after2=after.reshape(-1)                                    #flatens the array conerts multidimensional array to 1D



#to iterate through multidimensional array 
b=np.array([[[11,12],[13,14]],[[14,15],[16,17]]])
#for i in np.nditer(b):                                     #different conditions can be applied in nditer method
    #print(i)

#data is not changed in the original array so needs to store the data called buffer done by flag argument
# for x in np.nditer(arr,flags=["buffered"],op_dtypes=["S"]): #to change datatype while iterating
#     print(x)
"""
List of all data types in NumPy and the characters used to represent them.
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
For i, u, f, S and U we can define size as well.
"""

#Enumeration means mentioning sequence number one by one
# for index,x in np.ndenumerate(b):
#     print(index,x)                                          #index is returned as tuple


#splits the array by split size if array has less size then end is adjusted accordingly unlike split()-gives error
#the dimension of split array is same as the original array.
splits=np.array_split(concat,4)    

arr=np.array([[1,2,3,4],[5,6,7,8]])
hsplits=np.hsplit(arr,2)                                      #horizontal array split for multidimensional arrays

#sorting
sort=np.sort(concat)                                          #sort() returns a copy so original array is unchanged unile array.sort()

searching=np.where(arr==4)                                    #search in numpy array. Returns index where(x,y) yields x for true condition and y for false
#binary search on sorted array to return value where the element should be inserted to maintain search order
searching=np.searchsorted(arr[1],4)                            #list of multiple values can be passed too
searching=np.searchsorted(arr[0],4,side="left")                
#side :If ‘left’,the index of the first suitable location found is given.
#If ‘right’, return the last such index. 
#If there is no suitable index, return either 0 or N (where N is the length of a).


#load file
filedata=np.genfromtxt('E:\\Programs\\Python\\Numpy\\numpy_dataset.txt',delimiter=',')
filedata=filedata.astype("int32")                             #to convert the datatype of data

#advanced indexing and boolean masking
data=filedata>10                                              #apply some condition returns boolean
data=filedata[filedata>10]                                    #return / filter values that satisfies the condition
var=data[[3,5,7]]                                             #accessing multiple elements by their index

#apply condition on column.axis=1 for rows
data=np.any(filedata>15,axis=0)                               #apply condition on column.any one value in column satisfies return true
data=np.all(filedata>15,axis=0)                               #all value in column satisfies only then return true
data=filedata[(filedata>15) & (filedata<20)]                  #apply multiple conditions
