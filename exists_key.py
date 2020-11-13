dict={"name":"Raju", "marks":56}
for  i in dict:
    if  "name" in i:
        print("name", "key is exists in dict ")
    elif "marks" in i:
        print("marks", "key is exists in dict")
    else:
        print("name","marks" ,"key is not exists in dict ")