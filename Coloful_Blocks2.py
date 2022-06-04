n,k = map(int, input().split())
 
a = 10**9+7
 
if n == 1:
 print(k)
elif n == 2:
 print((k*(k-1))%a)
else:
 if k == 2:
  print(0)
 else:
  print((k*(k-1)*pow(k-2,n-2,a))%a)