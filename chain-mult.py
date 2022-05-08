    
def compute(i,j,A,d):

    if A[i][j]!="-":


        return A[i][j]

    val=[]
    for k in range(i,j):

        val.append(compute(i,k,A,d)+d[i-1]*d[k]*d[j]+compute(k+1,j,A,d))

    A[i][j]=min(val)

    return A[i][j]



d=[2,5,4,10,2,5,3]
A=[]

for i in range(len(d)):

    A.append([])

    for j in range(len(d)):

        A[i].append("-")



for m in range(1,len(A[0])):
    A[m][m]=0



print(compute(1,6,A,d))


for x in A:


    print(x)
    