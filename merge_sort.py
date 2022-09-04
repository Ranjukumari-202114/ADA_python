def merge(low,high):
    result = [] # to store result
    i ,j=0,0
    # merging algorithm
    while i<len(low) and j < len(high):  
        if(low[i]<high[j]):
           result.append(low[i])
           i +=1
        else:
           result.append(high[j]) 
           j +=1
    result +=low[i:]
    result +=high[j:]
    return result


def mergesort(lst):
    if(len(lst)<=1): # return is lst has only one value, cause it is already sorted
       return lst
    mid = int(len(lst)/2)
    low = mergesort(lst[:mid]) #calling function recursively
    high = mergesort(lst[mid:])#calling function recursively
    return merge(low,high)

arr = [1,3,-1,0,4,9,5,-7,-6,4]
print(mergesort(arr))