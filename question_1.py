# find the square of every list element
li=[]
n=int(input("enter the Number:"))

for i in range(0,n):
    ele = int(input())
  
    li.append(ele)
   
print(li)

for i in li:
    print(i*i)
