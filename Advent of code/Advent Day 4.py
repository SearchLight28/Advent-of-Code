def add(ranges):
    pairs=0
    ends=[]
    for i in ranges:
        i=i.strip("\n")
        i=i.strip("-")
        i=i.strip(",")
       # print(i)
        ends.append(i.split(","))
    for i in range(len(ends)):
        for a in range(2):
            #print(ends[i][1])
            ends[i][a]=ends[i][a].split("-")

        
        
    print(ends)
    result=list(map(check, ends))
    for i in result:
        if i==True:
            pairs+=1
    print(result)
    print(pairs)

def check(ends):
    #print(ends)
 #   if (int(ends[0][0])>=int(ends[1][0]) and int(ends[0][1])<=int(ends[1][1])) or (int(ends[1][0])>=int(ends[0][0]) and int(ends[1][1])<=int(ends[0][1])):
  #      return True
    for i in range(int(ends[0][0]),int(ends[0][1])+1):
        for a in range(int(ends[1][0]),int(ends[1][1])+1):
            if a==i:
                return True
    else:
        return False
    
        
    #print(ends)
    








file=open('day4.txt','rt')
add(file)
#find(file) 