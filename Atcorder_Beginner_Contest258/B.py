n=int(input())
Map=[]
for i in range(n):
    A=input()
    B=[]
    for j in range(n):
        B.append((A[j]))
    Map.append(B)
Max=0
for i in range(n):
    for j in range(n):
        a=''
        b=''
        c=''
        d=''
        e=''
        f=''
        g=''
        h=''
        tmp_a_i=i#右
        tmp_b_i=i#下
        tmp_c_i=i#右下
        tmp_d_i=i#左下
        tmp_a_j=j
        tmp_b_j=j
        tmp_c_j=j
        tmp_d_j=j
        tmp_e_j=j#左
        tmp_f_i=i
        tmp_f_j=j#左上
        tmp_g_i=i#上
        tmp_h_i=i
        tmp_h_j=j#右上
        a+=Map[i][j]
        b+=a
        c+=a
        d+=a
        e+=a
        f+=a
        g+=a
        h+=a
        for k in range(n):
            if tmp_a_j+1>n-1:
                tmp_a_j=0
            else:
                tmp_a_j+=1
            if tmp_b_i+1>n-1:
                tmp_b_i=0
            else:
                tmp_b_i+=1  
            if tmp_c_i+1>n-1:
                tmp_c_i=0
            else:
                tmp_c_i+=1
            if tmp_c_j+1>n-1:
                tmp_c_j=0
            else:
                tmp_c_j+=1
            if tmp_d_j-1<0:
                tmp_d_j=n-1
            else:
                tmp_d_j-=1
            if tmp_d_i+1>n-1:
                tmp_d_i=0
            else:
                tmp_d_i+=1
            if tmp_e_j-1<0:
                tmp_e_j=n-1
            else:
                tmp_e_j-=1
            if tmp_f_j-1<0:
                tmp_f_j=n-1
            else:
                tmp_f_j-=1
            if tmp_f_i-1<0:
                tmp_f_i=n-1
            else:
                tmp_f_i-=1
            if tmp_g_i-1<0:
                tmp_g_i=n-1
            else:
                tmp_g_i-=1
            
            if tmp_h_j+1>n-1:
                tmp_h_j=0
            else:
                tmp_h_j+=1
            if tmp_h_i-1<0:
                tmp_h_i=n-1
            else:
                tmp_h_i-=1
            if tmp_a_j==j:
                break
            a+=Map[tmp_a_i][tmp_a_j]
            b+=Map[tmp_b_i][tmp_b_j]
            c+=Map[tmp_c_i][tmp_c_j]
            d+=Map[tmp_d_i][tmp_d_j]
            e+=Map[i][tmp_e_j]
            f+=Map[tmp_f_i][tmp_f_j]
            g+=Map[tmp_g_i][j]
            h+=Map[tmp_h_i][tmp_h_j]
        if Max<int(a):
            Max=int(a)
        if Max<int(b):
            Max=int(b)
        if Max<int(c):
            Max=int(c)
        if Max<int(d):
            Max=int(d)
        if Max<int(e):
            Max=int(e)
        if Max<int(f):
            Max=int(f)
        if Max<int(g):
            Max=int(g)
        if Max<int(h):
            Max=int(h)
        
print(Max)