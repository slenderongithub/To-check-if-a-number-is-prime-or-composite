#WAP to check if a number is prime or composite 

n= int(input("enter any number to check if its composite or prime: "))
f=0
for i in range (1,n+1):
    if(n%i==0):
        f=f+1
if (f>2):
    print(n, "is composite")
else:
    print(n, " is prime")