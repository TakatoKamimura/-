from scipy.spatial import distance
import math
n=int(input())
s=list(input())
t=list(input())

count=math.floor(distance.hamming(s,t)*n)
if count%2==1:
    print(-1)
else:
    s_count=0
    t_count=0
    ans=''
    count=count//2
    for i in range(n):
        if s[i]!=t[i]:
            if s[i]=='1' and s_count<count:
                ans+='0'
                s_count+=1
            
            elif s[i]=='1' and s_count==count:
                ans+='1'
            elif s[i]=='0' and t_count<count:
                ans+='0'
                t_count+=1
            elif s[i]=='0' and t_count==count:
                ans+='1'
        else:
            ans+='0'
    print(ans)

    