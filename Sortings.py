class Sortings:
    """
    This Module contains four basic sorting algorithms.
    Selection sort, iterative and recursive Insertion sort, Merge sort, Quicksort.
    import this module: from Sortings import * 
    create an object and any sorting algorithm can be used by calling it as a method. c 
    """
    
    def SelectionSort(self,L):
        n = len(L)
        if n < 1:
            return(L)
        for i in range(n):
            mpos = i
            for j in range(i+1, n):
                if L[j] < L[mpos]:
                    mpos = j
            (L[i],L[mpos]) = (L[mpos], L[i])
        return(L)

    def InsertionSort(self,L):
        n = len(L)
        if n < 1:
            return(L)
        for i in range(n):
            j=i
            while(j > 0 and L[j] < L[j-1]):
                (L[j], L[j-1]) = (L[j-1], L[j])
                j = j-1
        return(L)

    def Insert(self,L, v):      #recursive method need self to be defined and the method to be called on itself
        n = len(L)              #only define when method is defined, later called by self.method
        if n==0:
            return([v])
        if v >= L[-1]:
            return(L+[v])
        else:
            return(self.Insert(L[:-1],v) + L[-1:])
    def ISort(self,L):
        n = len(L)
        if n < 1:
            return(L)
        L = self.Insert(self.ISort(L[:-1]), L[-1])
        return(L)

    def Merge(self,A, B):
        (m,n) = (len(A), len(B))
        (C,i,j,k) = ([],0,0,0)
        while k < m+n:
            if i == m:
                C.extend(B[j:])
                k = k + (n-j)
            elif j == n:
                C.extend(A[i:])
                k = k + (n-i)
            elif A[i] < B[j]:
                C.append(A[i])
                (i,k) = (i+1,k+1)
            else:
                C.append(B[j])
                (j,k) = (j+1,k+1)
        return(C)
    def MergeSort(self,A):
        n = len(A)
        if n <= 1:
            return(A)
        L = self.MergeSort(A[:n//2])
        R = self.MergeSort(A[n//2:])
        B = self.Merge(L, R)
        return(B)

    def QuickSort(self,L, l,r):
        if(r-l <= 1):
            return(L)
        (pivot,lower,upper) = (L[l], l+1,l+1)
        for i in range(l+1, r):
            if L[i] > pivot:
                upper = upper+1
            else:
                (L[i], L[lower]) = (L[lower], L[i])
                (lower, upper) = (lower+1, upper+1)
        (L[l], L[lower-1]) = (L[lower-1], L[l])
        lower = lower-1
        self.QuickSort(L, l, lower)
        self.QuickSort(L, lower+1, upper)
        return(L)
