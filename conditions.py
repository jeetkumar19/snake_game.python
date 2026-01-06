#conditionals
a=7
if a>0:
    print("positive")
#
a=-7
if a>0:
    print("postive") #nothing will print because condition is not defined.

#
a=34
if a>23:
    print("positive")

else:               #after else no codition will applied.
    print("negative")

#
a=0
if a>0:
    print("positive")
else:
    print("negative")

#
a=int(input("enter a number:"))
if a>0:
    print("positive")
elif a==0:
    print("a is nethier positive nor negative")

elif a<0:
    print("negative")

#write a python program of max of two number

k=int(input("enter first number:"))
c=int(input("enter second number:"))
if k>c:
    print(k,"is greater")
elif k<c:
    print(c,"is greater")
elif k==c:
    print("both are same")


#write a python program of max of three number
    
k=int(input("enter first number:"))
c=int(input("enter second number:"))
f=int(input("enter third number:"))
    
if k>c and k>f:
    print(k,"is greater")
elif c>k and c>f:
    print(c,"is greater")
else:
    print(" f is greater")

#write a program of even or odd
x=int(input("enter a number"))
if x% 2==0:
    print("x is even")
else:
    print("x is odd")

    
    


    


