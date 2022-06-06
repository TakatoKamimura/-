from struct import unpack, pack
import matplotlib.pyplot as plt
i_num = []
Val = []
with open('信号処理.wav', 'rb') as f:
    header=f.read(44)#音声データまでを読み込む
    for i in range(96256//2):#過大位置で確認したデータチャンクサイズ分のデータを2byteずつ読み込む
        i_num.append(i)
        Val.append(unpack("h", f.read(2))[0])

data_2=[]#量子化データ
data_4=[]#量子化データ

Max = max(Val)
Min = min(Val)
for i, x in enumerate(Val):
    norm = int((x - (Max + Min)/2) * 23170*2/(Max-Min)) #正規化
    if Val[i] < 0: #負の数
        data_2.append(((norm >> 8)+1) << 8)
        data_4.append(((norm >> 12)+1) << 12)
    else: #正の数
        data_2.append((norm >> 8) << 8)
        data_4.append((norm >> 12) << 12)

with open('data_2.wav','wb') as f:
    f.write(header)
    for i, x in enumerate(data_2):
        f.write(pack("h",x))


with open('data_4.wav','wb') as f:
    f.write(header)
    for i, x in enumerate(data_4):
        f.write(pack("h",x))



