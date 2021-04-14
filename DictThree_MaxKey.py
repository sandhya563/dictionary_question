my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
list=[]
max1=0
max2=0
max3=0
for key in my_dict:
    for value in my_dict:
        if my_dict[key]>max1:
            max1=my_dict[key]
            c=key
        elif max1>my_dict[value] and max2<my_dict[value]:
            max2=my_dict[key]
            d=key
        elif max2>my_dict[value] and max3<my_dict[value]:
            max3=my_dict[key]
            e=key
list.append(c)
list.append(d)
list.append(e)
print(list)
