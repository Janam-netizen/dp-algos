import math



def fw(g_i,k):

    print("---------------------------------------------------------------")

    for x in g_i:

        print(x)

    if k>len(g_i)-1:

        return g_i

    g_f=[]

    for i in range(len(g_i)):

        g_f.append([])

        for j in range(len(g_i[0])):

            if(i==k or j==k):

                g_f[i].append(g_i[i][j])
            else:

                g_f[i].append(min(g_i[i][k]+g_i[k][j],g_i[i][j]))

        
    return fw(g_f,k+1)

g=[[0,4,math.inf,-2,math.inf,math.inf],
   [4,0,3,math.inf,math.inf,math.inf],
   [math.inf,2,0,math.inf,math.inf,-2],
   [math.inf,math.inf,math.inf,0,3,math.inf],
   [math.inf,-1,math.inf,3,0,4],
   [math.inf,math.inf,math.inf,math.inf,4,0]]


fw(g,0)






        
    

    

    