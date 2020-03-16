def valid_parentheses(string):
    countx=0
    county=0
    flag=False
    countres=0
    for i in string:
        if i =="(":
            countx+=1
        if i==")":
            county+=1
        if i==")" and countx>=county:
            countres+=1
            
    if (countres>=0 and countx == countres and county==countres and countx==county):
        flag=True
    else:
        flag=False
    return flag

print(valid_parentheses("()(ljekm(disrn)jospzfyo)(rvmo)"))
'''
Test.assert_equals(valid_parentheses("  ("),False)
Test.assert_equals(valid_parentheses(")test"),False)
Test.assert_equals(valid_parentheses(""),True)
Test.assert_equals(valid_parentheses("hi())("),False)
Test.assert_equals(valid_parentheses("hi(hi)()"),True)
'''