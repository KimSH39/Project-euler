a=0
b=1
c=a+b
result=0
while c<4000000:
    c=a+b
    a=b
    b=c
    if c%2==0:
        result += c    

print(result)