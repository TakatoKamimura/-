class A:
    def __init__(self,count1,count2,ans):
        self.count1=count1
        self.count2=count2
        self.ans=ans
    def get_ans(self):
        return self.ans
    def get_count1(self):
        return self.count1
    def get_count2(self):
        return self.count2
        
N=int(input())
Answer=[]
if N%2>0:
    print()
else:
    count2=N//2
    count1=count2-1
    V='('
    a=A(count1,count2,V)
    Answer.append(a)
    for i in range(N-1):
        s=[]
        for j in range(len(Answer)):
            if Answer[j].get_count1()==Answer[j].get_count2():
                count=Answer[j].get_count1()-1
                l=Answer[j].get_ans()
                l=l+'('
                a=A(count,Answer[j].get_count1(),l)
                s.append(a)
            else:
                count1=Answer[j].get_count1()
                count2=Answer[j].get_count2()
                l=Answer[j].get_ans()
                if count1!=0:
                    c=count1-1
                    d=count2-1
                    a=A(count1-1,count2,l+'(')
                    b=A(count1,count2-1,l+')')
                    s.append(a)
                    s.append(b)
                else:
                    b=A(count1,count2-1,l+')')
                    s.append(b)
        Answer=s
for i in range(len(Answer)):
    print(Answer[i].get_ans())