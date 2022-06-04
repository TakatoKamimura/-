def binary_search(data, value):
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2            # 探索する範囲の中央を計算
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return -1            # 見つからなかった場合

N=int(input())
A=list(map(int,input().split()))

s=sum(A)/10

Sum_List=[]
A=A+A
tmp=0
for i in range(2*N):
    tmp+=A[i]
    Sum_List.append(tmp)
flag=0
for i in range(2*N):
    if binary_search(Sum_List,Sum_List[i]+s)!=-1:
        print('Yes')
        flag=1
        break
if flag==0:
    print('No')
    