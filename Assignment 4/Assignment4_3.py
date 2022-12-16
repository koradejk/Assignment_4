
from functools import*
n=int(input("Enter the length of list:"))
lis=[]
for i in range(0,n):
    element=int(input("Enter the element:"))
    lis.append(element)
print("The list of given number is:",lis)
print(lis)
def mark(m):
    if m>=70:
        return True
result=list(filter(mark,lis))
print("The no greater than or equal to 70",result)
result=list(map(lambda n:n+10,result))
print("The no by Adding 10:",result)
result=reduce(lambda n,m:n+m,result)
print("The Number after reduction:",result)
def mark(m):
    if m<=90:
        return True
result=list(filter(mark,lis))
print("The no less than or equal to 90",result)
result=list(map(lambda n:n+10,result))
print("The no by Adding 10:",result)
result=reduce(lambda n,m:n+m,result)
print("The Number after reduction:",result)


