# removing dublicate number but store in same order

num=[1, 4, 2, 3, 2, 1, 5]
new_num=[]
for i in num:
    if i not in new_num:
        new_num.append(i)

print(new_num)
