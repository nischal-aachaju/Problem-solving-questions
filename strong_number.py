# 145 = 1! + 4! + 5!
# Input: 145
# Output: Strong Number


num=144
input_num=num

def factorial(num):
    factorian_num=1
    for i in range(1,num+1):
        factorian_num*=i
    return factorian_num

output=0
while True:
    s=input_num%10
    output+=factorial(s)
    input_num//=10
    if input_num==0:
        break
if num==output:
    print(f"{num} is strong number")
else:
    print(f"{num} is not strong number")
    