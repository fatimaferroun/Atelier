def fact(n)
    rest=1
    for i in range n:
        rest*=i
        return rest
    sum=fact()
    sum=fact(1)/1+fact(2)/2+fact(3)/3+fact(4)/4+fact(5)/5
    print("sum=",sum())