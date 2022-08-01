n = input()
x = int(n)
n2 = str(x*2)
m = 2*x

ans = []
s = -1
while(x > 0):
    if x >= 4:
        ans.append("4")
        x -= 4
    else:
        s = x
        x = 0
print(m)
if not s == -1:
    print(s, end="")
    print("".join(ans))
else:
    print("".join(ans))
