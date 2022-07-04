n=int(input())
if n<60:
    print("21:",end='')
    if n<10:
        s='0'
        s+=str(n)
        print(s)
        exit()
    else:
        print(n)
else:
    print("22:",end='')
    n=n-60
    if n<10:
        s='0'
        s+=str(n)
        print(s)
        exit()
    else:
        print(n)