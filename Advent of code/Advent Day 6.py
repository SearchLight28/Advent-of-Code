def check3(file):
    q=[]
    count=4
    done=True
    for i in file:
        i=i.strip("\n")
        q.append(i)
    for i in range(len(q)):
        done=True
        count=4
        while done:
            if q[i][0]==q[i][1] or q[i][0]==q[i][2] or q[i][0]==q[i][3] or q[i][1]==q[i][2] or q[i][1]==q[i][3] or q[i][2]==q[i][3]:
                q[i]=q[i][1:]
                count+=1
            else:
                print(count)
                done=False
                
def check2(file):
    q=[]
    newQ=[]
    count=14
    done=True
    for i in file:
        i=i.strip("\n")
        q.append(i)
        
    for i in range(len(q[0])):
        if len(q[0][i:count])==len(set(q[0][i:count])):
            print(count)
            return
        else:
            count+=1
   # for i in range(len(q)):
    #    done=True
     #   count=4
      #  while done:
       #     if q[i][0]==q[i][1] or q[i][0]==q[i][2] or q[i][0]==q[i][3] or q[i][1]==q[i][2] or q[i][1]==q[i][3] or q[i][2]==q[i][3]:
        #        q[i]=q[i][1:]
         #       count+=1
          #  else:
           #     print(count)
            #    done=False

                
            
    


file=open('day6.txt','rt')
check2(file)