import copy
def path_finder(maze):
    nwmaze=maze.split("\n")
    xt=len(nwmaze[0])
    yt=len(nwmaze)
    solution_paths=[]
    solution_paths.append([[0,0]])
    found=False
    while(True):
        old=add_any_path_open(xt,yt,nwmaze, solution_paths)
        found=ending_found(xt,yt, solution_paths)
        if(found==True):
            return True
        if(isStucked(old,solution_paths)==True):
            return False
        

def ending_found(xt,yt,solution_paths):
    for path in solution_paths:
        if [xt-1,yt-1] == path[-1]:
            return True
    return False

def add_any_path_open(xt,yt,nwmaze,solution_paths):

    tempsol=copy.deepcopy(solution_paths)
    for posactualpath in range(len(solution_paths)):
        samepath=1
        actualpath=solution_paths[posactualpath][len(solution_paths[posactualpath])-1]
        print(actualpath)

        x=actualpath[0] #ultima posicio de cada cami del array (x)
        y=actualpath[1] #ultima posicio de cada cami del array (y)

        if(x+1 <xt and nwmaze[y][x+1]=="."):
            if samepath==1:
                if isAlreadyInThePath([x+1,y], solution_paths)==False:
                    solution_paths[posactualpath].append([x+1,y])
                    samepath=0
            else:
                if isAlreadyInThePath([x+1,y] , solution_paths)==False:
                    tmp=copy.deepcopy(tempsol)
                    tmp.append([x+1,y])
                    solution_paths.append(tmp[0])
                    samepath=0
        if(y+1 <yt and nwmaze[y+1][x]=="."):
            if samepath==1:
                if isAlreadyInThePath([x,y+1], solution_paths)==False:
                    solution_paths[posactualpath].append([x,y+1])
                    samepath=0
            else:
                if isAlreadyInThePath([x,y+1], solution_paths)==False:
                    tmp=copy.deepcopy(tempsol)
                    tmp[posactualpath].append([x,y+1])
                    solution_paths.append(tmp[posactualpath])
                    samepath=0
        if(x-1 >=0 and nwmaze[y][x-1]=="."):
            if samepath==1:
                if isAlreadyInThePath([x-1,y], solution_paths)==False:
                    solution_paths[posactualpath].append([x-1,y])
                    samepath=0
            else:
                if isAlreadyInThePath([x-1,y], solution_paths)==False:
                    tmp=copy.deepcopy(tempsol)
                    tmp[posactualpath].append([x-1,y])
                    solution_paths.append(tmp[posactualpath])
                    samepath=0
        if(y-1 >=0 and nwmaze[y-1][x]=="."):
            if samepath==1:
                if isAlreadyInThePath([x,y-1], solution_paths)==False:
                    solution_paths[posactualpath].append([x,y-1])
                    samepath=0
            else:
                if isAlreadyInThePath([x,y-1], solution_paths)==False:
                    tmp=copy.deepcopy(tempsol)
                    tmp[posactualpath].append([x,y-1])
                    solution_paths.append(tmp[posactualpath])
                    samepath=0
    return tempsol
def isStucked(old,solution_paths):
    n=sum(len(path) for path in old)
    m=sum(len(path) for path in solution_paths)
    if(n==m):
        return True
    else:
        return False
def isAlreadyInThePath(actual, solution_paths):
    for path in solution_paths:
        if actual in path:
            return True
    return False

a = "\n".join([
'.W...',
'.W...',
'.W.W.',
'...W.',
'...W.'])

print(path_finder(a))# True)
