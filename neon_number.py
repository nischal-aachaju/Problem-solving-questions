# Input: 9 → 9² = 81 → 8+1 = 9
# Output: Neon Number

num=19
sq_num=num**2
digit_sum=0
while True:
    s=sq_num%10
    digit_sum+=s
    sq_num//=10
    if sq_num==0:
        break
if num==sum:
    print(f" {num} is Neon number")
else:
    print(f" {num} is not Neon number")
