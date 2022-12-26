class Setup():
    def __init__(self,items):
        totalC=[]
        total=0
        foods=[]
        newfoods=[]
        aFoods=[]
        for i in items:
            i=i.strip('\n')
            if i!="":
                foods.append(i)
        #foods=items.split("\n\n")
        print(foods)
        count=0
        for i in foods:
            newfoods=i.split("\n")
            aFoods.append(newfoods)
        print(aFoods)
        for i in aFoods:
            for a in i:
                a=int(a)
                total=a+total
            totalC.append(total)
            total=0
        print(totalC)
        self.compare(totalC,total)
    def compare(self,totalC,total):
        maxfoods=totalC[0]
        top3=[]
        for i in range(3):
            for i in range(len(totalC)-1):
                if maxfoods<totalC[i+1]:
                    maxfoods=totalC[i+1]
            top3.append(maxfoods)
            print(maxfoods)
            if maxfoods in totalC:
                totalC.remove(maxfoods)
                maxfoods=0
        maxfoods=0
        for i in top3:
            maxfoods=i+maxfoods
        print(maxfoods)
    
        print(top3)


foods=open('foods.txt','rt')
Setup(foods)