# list = [0,1,2,3,4,5]
# def moveList(l,e):
#     l.insert(len(list),e)
#     l.remove(l[0])
#     print(l)

# moveList(list,6)


# import random
# list = [0,1,2,3,4,5]
# def instMeth(l,e):
#     r = random.randint(0,5)
#     l.insert(r,e)
#     print(l)

# instMeth(list,8)


list = ["a","a","a","b","b","b","c","c","c"]
def remStr(p):
    list.pop(p)
    a =  0
    b =  0
    c =  0
    for e in range (int(len(list))):
        if(list[e] == "a"):
            a+=1
            
        if(list[e] == "b"):
            b+=1
            
        if(list[e] == "c"):
            c+=1
    
    while find:




    if(0 < a):
        text = f"il reste {a} fois lettre a"
    elif(0 < b):
        text = f"il reste {a} fois lettre a"
    elif(0 < c):
        text = f"il reste {a} fois lettre a"



    print(a)
    print(b)
    print(c)             
    if(0 < a):
        print(f"il reste {a} fois lettre a")
    elif(0 < b):
        print(f"il reste {b} fois lettre a")
    elif(0 < c):
        print(f"il reste {c} fois lettre a")

remStr(5)