
from functools import*
n=int(input("Enter the length of list:"))
lis=[]
for i in range(0,n):
    element=int(input("Enter the element:"))
    lis.append(element)
print("The list of given number is:",lis)
print(lis)
evenlis=list(filter(lambda no:(no%2==0),lis))
print("list after filter using lambda:",evenlis)
maplis=list(map(lambda no:no**2,evenlis))
print("list after map using lambda:",maplis)
sum=reduce(lambda a,b:a+b,maplis)
print("output of reduce:",sum)
