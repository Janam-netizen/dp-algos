

'''
gram->grammar

get_var() return the set of variables in the gramar that yield the corrosponding rule in one step 



'''
def get_var(gram,rule):
    s=set()

    for var in gram:

        if rule in gram[var]:

            s=s.union({var})

    return s





'''
s1 and s2 are two arbitrary set of variables.

It returns the the cross product of s1 and s2

s1={'A','B'}

S2={'C','D'}

cross_prod(s1,s2)={'AC','AD','BC','BD'}
'''
def cross_prod(s1,s2):

    s=set()

    if len(s1)==0 or len(s2)==0:

        return set()

    for x in s1:

        for y in s2:
            
            s=s.union({x+y})

    return s

'''
CP-Set of rules of the form XY or a, where X and Y are variables in the grammar and a is the input alphabet 

gram:grammar in CNF
'''
def gen_set(gram,CP):

    s=set()
    for rule in CP:

        s=s.union(get_var(gram,rule))

    return s



'''

cyk(i,j,A,gram,s)

s-input string
gram-grammar
A-Table that maps s[i:j] to some set of vars

such that 1<=i<=n  and i<=j<=n
'''

def cyk(i,j,A,gram,s):

    if A[i][j]!="-":


        return A[i][j]

    vars=set()
    for k in range(i,j):

        vars=vars.union(gen_set(gram,cross_prod(cyk(i,k,A,gram,s),cyk(k+1,j,A,gram,s))))

    A[i][j]=vars

    return vars

A=[]
gram={"S":["AA","BB","a","b"],
"A":["AE","BC","a"],
"B":["BE","AD","b"],
"C":["AA","CE"],
"D":["BB","DE"],
"E":["AB","BA","EE"]}  
s="aaabab"

print(len(s))
for i in range(len(s)):

    A.append([])

    for j in range(len(s)):

        print(j)

        if(i==j):

            A[i].append(get_var(gram,s[i]))

        else:

            A[i].append("-")




for x in A:

    print(x)


cyk(0,len(s)-1,A,gram,s)

for x in A:

    print(x)














