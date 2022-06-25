n = int(input())
s = input()
 
mod = 10**9+7
 
a = [0]*7
 
for i in range(n):
 if s[i] == 'a':
  a[0] += 1
 elif s[i] == 't':
  a[1] += a[0]
 elif s[i] == 'c':
  a[2] += a[1]
 elif s[i] == 'o':
  a[3] += a[2]
 elif s[i] == 'd':
  a[4] += a[3]
 elif s[i] == 'e':
  a[5] += a[4]
 elif s[i] == 'r':
  a[6] += a[5]
 
print(a[-1]%mod)