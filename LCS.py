def LCS(A,B,a,b):
    Q=[[0 for i in xrange(b+1)]for j in xrange(a+1)]

    for i in xrange(a+1):
        for j in range(b+1):
            if i==0 or j==0:
                Q[i][j]=0
            elif A[i-1]==B[j-1]:
                Q[i][j]=Q[i-1][j-1]+1
            else:
                Q[i][j]=max(Q[i-1][j],Q[i][j-1])

    v=Q[a][b]
    S=[""]*(v+1)
    S[v]="\0"

    i=a
    j=b
    while i>0 and j>0:
        if A[i-1]==B[j-1]:
            S[v-1]=A[i-1]
            i=i-1
            j=j-1
            v=v-1
        elif Q[i-1][j]>Q[i][j-1]:
            i=i-1
        else:
            j=j-1
    print "Least Common Subsequence of "+ A + " and " + B + " is "+ "".join(S)
A=input("Enter the first string in quotes:")
B=input("Enter the second string in quotes:")
a=len(A)
b=len(B)
LCS(A,B,a,b)
