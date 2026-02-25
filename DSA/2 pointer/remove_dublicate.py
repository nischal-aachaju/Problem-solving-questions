a=[1,1,2,2,3,4,4]

def fun(head):
    i=1
    j=0
    while i<len(head):
        
        if head[i]==head[i-1]:
            i+=1
        else:
            head[j+1]=head[i]
            i+=1
            j+=1
    return head[:j+1]

print(fun(a))

