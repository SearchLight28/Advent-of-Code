def sort(ruck):
    items=[]
    values=[]
    count=0
    count2=0
    items.append([])
    for i in ruck:
        #print(i)
        i=i.strip("\n")
        items[count2].insert(2, i)
        count+=1
        if count==3:
            items.append([])
            count=0
            count2+=1
    items.pop(-1)
    #print(items)
    for i in items:
        #prior=priority(i)
        prior=priority2(i)
        #print(prior)
        a=value(prior)
        values.append(a)
    print(sum(values))

def priority(item):
    ruck=[]
    length=len(item)
    ruck.append(item[:length//2])
    ruck.append(item[length//2:])
    #print(ruck)
    for i in ruck[0]:
        for a in ruck[1]:
            if i==a:
                return a
            
def priority2(items):
    count=0
    let=""
   # print(items)
    for i in items[0]:
        for a in items[1]:
            for b in items[2]:
                if i==b and i==a:
                    let=i
    #print(let)
    return let
            
        
def value(prior):
    if prior!=prior.lower():
        prior=ord(prior)
        prior-=38
    else:
        prior=ord(prior)
        prior-=96
    #print(prior)
    return prior
            
        
    
file=open('day3.txt','rt')
sort(file)