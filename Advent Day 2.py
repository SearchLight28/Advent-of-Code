class Setup():
    def __init__(self):
        score=0
        choice=0
        op=[]
        options=open('Day2.txt','rt')
        for i in options:
            i=i.strip("\n")
            op.append(i)
       
                
        for i in op:
            if i[2]=="X":
                if i[0]=="A":
                    choice=3
                elif i[0]=="B":
                    choice=1
                elif i[0]=="C":
                    choice=2
                score=score+choice
            if i[2]=="Y":
                if i[0]=="A":
                    choice=1
                if i[0]=="B":
                    choice=2
                if i[0]=="C":
                    choice=3
                score=score+choice+3
            if i[2]=="Z":
                if i[0]=="A":
                    choice=2
                if i[0]=="B":
                    choice=3
                if i[0]=="C":
                    choice=1
                score=score+choice+6
                #print(score)
                
        print(score)
                
Setup()