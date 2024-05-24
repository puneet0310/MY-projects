def SelectionSort(l):
    n = len(l)
    if n<1:
        return(l)
    for i in range(n):
        mpos=i
        for j in range (i+1,n):
            if l[j]<l[mpos]:
                mpos=j
        (l[i],l[mpos])=(l[mpos],l[i])
    return(l)

def insertionSort(l):
    n=len(l)
    if n<1:
        return(l)
    for i in range(n):
        j=i
        while(j>0 and l[j]<l[j-1]):
            (l[j],l[j-1])=(l[j-1],l[j])
            j=j-1
    return(l)


def Merge(A,B):
    (m,n)=(len(A),len(B))
    (C,i,j,k)=([],0,0,0)
    while k <m+n:
        if i==m:
            C.extend(B[j:])
            k=k+(n-j)
        elif j==n:
            C.extend(A[i:])
            k=k+(n-i)
        elif A[i]<B[j]:
            C.append(A[i])
            (i,k)=(i+1,k+1)
        else:
            C.append(B[j])
            (j,k)=(j+1,k+1)
        return(C)
def MergeSort(A):
    n=len(A)
    if n<=1:
        return(A)
    L=MergeSort(A[:n//2])
    R=MergeSort(A[n//2:])
    B=Merge(L,R)
    return(B)
l=[23,12,34,54,65,89]
print(SelectionSort(l))
print("INSERTION SORT HAPPENING")
print(insertionSort(l))
print("MERGE SORT")
for i in l:
    print(MergeSort(l))
