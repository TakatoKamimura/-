# cubic cake
import math
a = list(map(int, input(). split()))
b = math.gcd(a[0], a[1])
c = math.gcd(a[1], a[2])
d = math.gcd(b, c)
print(str((a[0]+a[1]+a[2])//d-3))
