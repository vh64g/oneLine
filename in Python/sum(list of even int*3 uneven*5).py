print(print(l:=input(),x:=[int(input()) for i in range(int(l))],y:=[i*3 if i%2==0 else i*5 for i in x], end="\r"),print(sum(y)))
