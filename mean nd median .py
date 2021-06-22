n=int(input("enter number of elements:"))
x=[int(input("enter x values:"))for i in range(n)]
print('x values are:',x)
mean=float(sum(x)/n)
print("mean of the given array is :",mean)
def bubblesort(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
bubblesort(x)
if(n%2!=0):
    p=int(n/2)
    median=x[p]
elif(n%2==0):
    p=int((((n-1)/2)+((n+1)/2))/2)
    median=x[p]
print("median:",median)
