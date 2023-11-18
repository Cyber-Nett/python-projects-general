a=int(input())
max=0
number=0
while a!=0:
    number=a%10
    if max<number:
        max=number
    print(number)
print(f"максимальна :  {number}")
