def function(move,crate):
    for i in move:
        for a in range(int(i[0])):
            crate[int(i[2])-1].append(crate[int(i[1])-1].pop())
    print(crate)
    word=""
    for i in crate:
        word=word+i[-1]
        #print(i[-1])
    print(word)
        
def function2(move,crate):
    for i in move:
        for a in range(int(i[0]),0,-1):
            crate[int(i[2])-1].append(crate[int(i[1])-1].pop(len(crate[int(i[1])-1])-a))
    print(crate)
    word=""
    for i in crate:
        word=word+i[-1]
        #print(i[-1])
    print(word)
    
def sort(file,crate):
    move=[]
    for i in file:
        i=i.strip("move ")
        i=i.strip("\n")
        move.append(i.split(" "))
    for i in range(len(move)):
        move[i].remove("from")
        move[i].remove("to")
    #print(move)
    function2(move,crate)

crate=[['J','H','G','M','Z','N','T','F'],['V','W','J'],['G','V','L','J','B','T','H'],['B','P','J','N','C','D','V','L'],['F','W','S','M','P','R','G'],['G','H','C','F','B','N','V','M'],['D','H','G','M','R'],['H','N','M','V','Z','D'],['G','N','F','H']]
file=open('day5.txt','rt')
sort(file,crate)