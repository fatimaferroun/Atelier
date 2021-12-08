str=input("entrer le mot:")
n=len(str)
frequence(str,n)
def chercher(matrice,a)
    ligne=0
    colone=0
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j]==a:
            ligne=i
            ocolone=j
            if ligne==0 and colone==0:
                print("la valeur",a,"n'existe pas dans la matrice")
            else:
                print("la valeur",a,"existe dans la matrice est sa position est i=",ligne+1,"j=",colone+1)
                tab=[[1,2,3],[4,5,6]]
                c=int(input("entrez le nombre recherché:\n"))