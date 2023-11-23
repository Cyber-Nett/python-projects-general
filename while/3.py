n=int(input('num: '))
a=n
c=0
while n!=0:
    n=n//10
    c+=1
if c%2==0:
    b=a//(10**(c/2))
    ce=a%(10**(c/2))
    if b==ce:
        while True:
            print('True')
elif c%2!=0:
    b=a//(10**((c+1)//2))
    ce=a%(10**((c-1)//2))
    if b==ce:
        while True:
            print('True')
else:
    print('False')



