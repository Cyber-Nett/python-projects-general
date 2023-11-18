a=int(input())
num=0
num=a
counter=0
while a>0:
    divnum = a//10
    print(divnum)
    a=(a-divnum)/10
    counter+=1
print(counter)
