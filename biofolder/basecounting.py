blist=input("give the genetic code data at most 1000nt")
A=0
C=0
T=0
G=0
if len(blist)>1000:
    print("sorry,this program are incapable of count more than 1000nt")
for indice in range(len(blist)):
    if blist[indice]=='A':
        A=A+1
    if blist[indice]=='C':
        C=C+1
    if blist[indice]=='T':
        T=T+1
    if blist[indice]=='G':
        G=G+1
print(A,"",C,"",G,"",T)

