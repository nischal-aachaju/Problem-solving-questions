# method 1
a=4
b=5
# before swap
print(a,b)
temp=a
a=b
b=temp
# after swap
print(a,b)

# method 2
x=10
y=20
# before swap
print(x,y)
x=x-y
y=x+y
x=y-x
# after swap
print(x,y)

# method 3 (Built in)
p=20
q=30
# before swap
print(p,q)
p,q=q,p
# after swap
print(p,q)