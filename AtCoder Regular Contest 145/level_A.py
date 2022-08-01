N = int(input())
S = input()
if S == "BA":
    print("No")
elif S[0] == "B" or S[-1] == "A":
    print("Yes")
else:
    print("No")
