#range- start value=0, stop value=10, step value-+1

x=[10,20,30]
print(x)

x=[1,2,3]
for i in x:
    print(i)
    
# for loop syntax:
# for variable name in sequence:(list,set,ramge,tuple)
#     statements

for i in range(10):  # start value=0 stop value=10, step value=+1
    print(i)
    
for i in range(1,20): #
    print(i)       
    
for i in range(0,20,2):
    print(i)
    
    
#write a program to print n natural numbers in run time:
n=int(input("enter n value:"))
for i in range(n):
    print(i)
    
    
# write a program to print characters in the string:
x= " rama krishna "
for i in (x):
    print(i)
    
   i=i+1for i in range(0,10):
    print(i,end=" ")
    
h="manikanta    satya"
for i in h:
    print(i)
    
# write a program to print skipping characters in the string:
a="snehitha"
n=len(a)
# to find out the length of the string:
#len-buildin function
print(len(a))
for i in range(0,n,2):
    print(a[i])

x=["apple","goa","mango"]
for i in x:
    print(i)
    
# write a program to print multiplication table:
n=int(input('enter n value:'))
for i in range(1,16):
    print(f"{n} * {i}={n*i}")
    
# nested while loop;
i=1
while(i<=3):
    print("manikanta")
    j=1
    while(j<=3):
        print("satya")
        j=j+1
    i=i+1
 
       
for i in range(1, 11): # 1-10
    for j in range(2, 4): # 2,3
        print(i * j, end=' ')
    print()

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
    
