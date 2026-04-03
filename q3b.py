def add_binary(a, b):
    sum1=0
    for i in range(len(a[-1:1:-1])):
        if a[-1:1:-1][i]=='1':
            sum1+=(2**i)
    for j in range(len(b[-1:1:-1])):
        if b[-1:1:-1][j]=='1':
            sum1+=(2**j)
    binary_sum=''
    while sum1>0:
        if sum1%2==1:
            binary_sum+='1'
        else:
            binary_sum+='0'
        sum1//=2
    binary_sum+='b0'
    return binary_sum[::-1]


print(add_binary("0b1010", "0b1011"))
'''
    Given two strings perform binary addition and return the result as a string
    '''