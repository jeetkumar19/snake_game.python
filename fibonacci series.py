#fibonacci series start with always zero;
x=int(input("enter a number:"))
a=-1
b=1
print(a)
print(b)

for i in range(x):
    c=a+b
    print(c)
    a=b
    b=c