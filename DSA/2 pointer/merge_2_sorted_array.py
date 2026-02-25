
# a=[1,3,5,7]
# b=[2,4,6,8,9,10]
# c=[]
# i=0
# j=0
# while i<len(a) and j<len(b):
#     if a[i]<=b[j]:        
#         c.append(a[i])
#         i+=1
#     elif b[j]<a[i]:
#         c.append(b[j])
#         j+=1

# while j< len(b):
#     c.append(b[j])
#     j+=1
# while i< len(a):
#     c.append(c[i])
#     i+=1
# print(c)


a=[1,3,5,7]
n=4
b=[2,4,6]
m=3
i=0
j=0
c=0
while i<n and j<m:
    if a[i]<=b[j]:        
        a.append(a[i])
        i+=1
    elif b[j]<a[i]:
        a.append(b[j])
        j+=1

while j< m:
    a.append(b[j])
    j+=1
while i< n:
    a.append(a[i])
    i+=1
a=a[n:]
print(a)