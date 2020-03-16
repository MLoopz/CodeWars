def solution(string,markers):
    print(string)
    print(markers)
    resp="".join(string)
    for m in markers:
        while True:
            ini=resp.find(m)
            fin=resp.find("\n",ini)
            if(ini<0):
                break
            if(fin<0):
                fin=len(resp)
            resp=resp[:ini].strip(' ').rstrip(' ')+resp[fin:].strip(' ').rstrip(' ')
    #your code here
    return resp

print(solution("apples, pears # and bananas\ngrapes\nbananas #!apples", ["#", "!"]))# "apples, pears\ngrapes\nbananas")