def sqare_fun(num1,num2):
    dict={}
    i=num1
    while i<=num2:
        multi=i*i
        dict[i]=multi
        i=i+1
    return dict
num1=int(input("enter any number"))
num2=int(input("enter any number"))
print(sqare_fun(num1,num2))
    