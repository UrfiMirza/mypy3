a=int(input("Enter Num a:"))
b=int(input("Enter Num b:"))
c=int(input("Enter Num c:"))
if a>b and a>c:
    print(f'{a} is biggest')
elif b>a and b>c:
    print(f'{b} is biggest')
else:
    print(f'{c} is biggest')

