

def merge_sort(A):
    if len(A)>1:
        q=len(A)//2
        left=merge_sort(A[:q])
        right=merge_sort(A[q:])
        return merge(left, right)
    return A

def merge(left, right):
    A=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            A.append(left[i])
            i=i+1
        else:
            A.append(right[j])
            j=j+1
    A+=left[i:]
    A+=right[j:]

    return A

test=[2,5,3,1,6,4]
print merge_sort(test)


    
    
