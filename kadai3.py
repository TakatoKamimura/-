from struct import unpack
import matplotlib.pyplot as plt
i_num = []
Val = []
with open('信号処理.wav', 'rb') as f:
    f.read(44)#音声データまでを読み込む
    for i in range(4410):#音声データ読み込み
        i_num.append(i)
        Val.append(unpack("h", f.read(2))[0])

data_2=[]#量子化データ
data_4=[]#量子化データ

Max = max(Val)
Min = min(Val)
for i, x in enumerate(Val):
    norm = int((x - (Max + Min)/2) * 23170*2/(Max-Min)) #正規化
    if Val[i] < 0: #負の数
        data_2.append((norm >> 8) << 8)
        data_4.append((norm >> 12) << 12)
    else: #正の数
        data_2.append((norm >> 8) << 8)
        data_4.append((norm >> 12) << 12)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, xlabel='Index', ylabel='Data Value')
ax1.plot(i_num,data_2)
ax1.grid(axis='both')
fig1.subplots_adjust(left=0.2)
fig1.savefig('report1-3_1.png')

fig2 = plt.figure()
ax2 = fig1.add_subplot(111, xlabel='Index', ylabel='Data Value')
ax2.plot(i_num,data_4)
ax2.grid(axis='both')
fig2.subplots_adjust(left=0.2)
fig2.savefig('report1-3_2.png')

