from functools import reduce

def Checkprime(lis):
    if lis==1:
        return False
    for i in range(2,lis):
        if lis%i==0:
            return False
    return True


def Multiply(a):
    return a*2

def Addition(a,b):
    return a+b

def main():
    n = int(input("Enter the length of list:"))
    lis = []
    for i in range(0, n):
        element = int(input("Enter the element:"))
        lis.append(element)
    print("The list of given number is:", lis)
    print(lis)
    a = lis
    #filter(function,list)
    newdata=list(filter(Checkprime,a))
    print("Data after filter:",newdata)
    Multiplydata=list(map(Multiply,newdata))
    print("data after map",Multiplydata)
    ret=reduce(Addition,Multiplydata)
    print("data after reduce",ret)
    print()

if __name__=="__main__":
    main()