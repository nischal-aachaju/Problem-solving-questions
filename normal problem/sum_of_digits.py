# first method
num=123456
output=6
sum=0

for i in str(num):
    sum=sum+int(i)

# print(sum)

# second method

n=123456
sum_n=0
while True:
    s=n%10
    sum_n+=s
    n=n//10
    if n==0:
        break

print(sum_n)