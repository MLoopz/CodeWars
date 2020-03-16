def iq_test(numbers):
    #your code here
    arrE=list()
    arrO=list()
    numbers=[int(i) for i in numbers.split()]
    for i in range(0,len(numbers)):
        if numbers[i]%2==0:
            arrE.append([numbers[i],i+1])
        else:
            arrO.append([numbers[i],i+1])
    return arrE[0][1] if len(arrE)<len(arrO) else arrO[0][1]

print(iq_test("2 4 7 8 10"))#3)
print(iq_test("1 2 2"))# 1)