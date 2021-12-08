
def fréquence_caractere(s,c):
    compteur=0
    for x in s:
        if x==c:
            compteur=compteur+1
            return compteur
        s="python is the most programming language"
        print(fréquence_caractere(s,'p'))