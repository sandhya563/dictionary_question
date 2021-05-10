list1=[{"item":"item1","amount":400},{"item":"item2","amount":300},{"item":"item1","amount":750},{"item":"item2","amount":50},{"item":"item3","amount":40}]
dict1 = {}
for i in list1:
    if i['item'] not in dict1:
        dict1[i['item']] = i['amount']
    else:
        dict1[i['item']] += i['amount']
print(dict1)