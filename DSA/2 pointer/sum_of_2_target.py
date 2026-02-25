
def twoSum( numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    i=0
    j=len(numbers)-1
    while i<j:
        sum=numbers[i]+numbers[j]
        if sum==target:
            return [i,j]
        elif(sum < target):
            i+=1
        else:
            j-=1
                
print(twoSum([2,3,4],6))