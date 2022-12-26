
def travel2(file):
    commands=[]
    stack=[]
    word=''
    dirs={}
    for i in file:
        i=i.strip("\n")
        commands.append(i)
    print(commands)
    for i in commands:
        if '$' in i:
            if i == '$ cd ..':
                stack.pop()
            elif 'cd' in i:
                stack.append(i[5:])
                if i[5:] not in dirs:
                    word=''.join(stack)
                    dirs[word]=0
        dirs[word]=dirs[word]+int(size(i))
    print(stack)
    print(dirs)
    
    
def checknum(string):
    return any(char.isdigit() for char in string)
def size(i):
    if checknum(i):
            if '.' in i:
                return i[:-5]
            else:
                return i[:-1]
    return 0
    

    
    
file=open('day7.txt','rt')
travel2(file)