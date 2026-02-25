def fun(arr):
    pos=[]
    neg=[]
    for i in arr:
        if i<0:
            neg.append(i*i)
        else:
            pos.append(i*i)
    neg=neg[::-1]
    return merge_arr_sorted(pos,neg)  
def merge_arr_sorted(arr1,arr2):
    i=0
    j=0
    merge_arr=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            merge_arr.append(arr1[i])
            i+=1
        else :
            merge_arr.append(arr2[j])
            j+=1
    return remove_dublicate(merge_arr)
def remove_dublicate(head):
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

print(fun(arr=[-4,-2,-1,0,3,4,5,7]))