a=int(input())
b=int(input())
c=int(input())

if a < b+c and b < c+a and c < a+b :
    if a == b == c : print("TRIANGOLO EQUILATERO",end="")
    elif a == b or a == c or b == c : print("TRIANGOLO ISOSCELE",end="")
    else : print("TRIANGOLO SCALENO",end="")
else: print("NO",end="")