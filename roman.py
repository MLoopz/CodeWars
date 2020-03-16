def solution(n):
    table={'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
    response=list()
    num=n
    while(num>0):
        for k,v in sorted(table.items(), key=lambda kv: kv[1], reverse=True) :
            if(num-v>=0):
                num=num-v
                response.append(k)
                break
    return ''.join(response)

print(solution(1349))