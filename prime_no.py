x=int(input("enter a number:"))
for i in range(2,x):
    if x % i==0:
        print(x," is not prime")
        break
    
else:
    print("its a prime no")
    