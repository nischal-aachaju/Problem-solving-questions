
lst= [10, 23, 45, 89,101 ,101,12]
first_largest=max(lst)
second_largest=min(lst)
for i in lst:
    if second_largest <= i and i < first_largest:
        second_largest=i
        
print(second_largest)