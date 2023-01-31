def snail(snail_map):
    x = len(snail_map)
    y = len(snail_map[x-1])
    startX = 0
    startY = 0
    response = []
    
    while startX <= x and startY <= y:
        for pos in range(startY,y):
            response.append(snail_map[startY][pos])
        startX+=1
        for pos in range(startX,x):
            response.append(snail_map[pos][y-1])
        y-=1
        for pos in range(y,startY, -1):
            response.append(snail_map[x-1][pos-1])
        x-=1
        for pos in range(x,startX, -1):
            response.append(snail_map[pos-1][startX-1])
        startY+=1
            
    return response

print(snail([[1,2,3],
         [4,5,6],
         [7,8,9]]))