def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
    
N=int(input())
a=prime_factorize(N)
if len(a)==1:
    print(0)
else:
    i=1
    while(True):
        if 2**i>=len(a):
            print(i)
            break
        else:
            i+=1
            

    