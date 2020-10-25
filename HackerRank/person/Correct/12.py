from functools import reduce
def processlists(f,l1,l2) :
	return f(l1,l2)
def addlists(l1,l2) : 
 temp = list(zip(l1,l2))
 result=[]
 for i in range(len(temp)) :
	result.append(reduce(lambda x,y : x+y,temp[i]))
 return result
def maxlist(l1,l2) :
 temp = list(zip(l1,l2))
 result=[]
 for i in range(len(temp)) :
	result.append(max(temp[i][0],temp[i][1]) )#checks for max and append that element.
 return result	
print("Enter lists of same length : ")
l1=list(eval(input("Enter list1 : ")))
l2=list(eval(input("Enter list2 : ")))
print("List containing sum of corresponding elements : ",processlists(addlists,l1,l2))
print("List containing maximums are : ",processlists(maxlist,l1,l2))

