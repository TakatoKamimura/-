class Node:
    def __init__(self,count,x,y):
        self.count=count
        self.x=x
        self.y=y

    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y
    
    def get_count(self):
        return self.count
    


H,W=map(int,input().split())
    
Map=[]

Answer=[]
for i in range(H):
    S=input()
    Map.append(S)
root=Node(1,0,0)
Answer.append(root)
Max=0
c=[[] for i in range(H)]
for i in range(H):
    for j in range(W):
        c[i].append(0)

while(True):
    if len(Answer)>0:
        a=Answer[0]
        Answer.pop(0)
        x=a.get_x()
        y=a.get_y()
        count=a.get_count()
        if c[x][y]<count:
            c[x][y]=count
        else:
            continue
        if Max<count:
            Max=count
        if x+1<H:
            if Map[x+1][y]=='.':
                new_node=Node(count+1,x+1,y)
                Answer.append(new_node)
                
        if y+1<W:
            if Map[x][y+1]=='.':
                new_node=Node(count+1,x,y+1)
                Answer.append(new_node)
    else:
        break
print(Max)

