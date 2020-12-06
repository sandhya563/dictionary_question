data={1:20,2:30,3:40,4:50,6:60}
def key_exits(x):
    if x in data:
        print("key is exits in dictionary")
    else:
        print("key is not exits in dictionary")
key_exits(6)
key_exits(10)