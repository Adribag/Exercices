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


# list = ["a","a","a","b","b","b","c","c","c"]
# def remStr(p):
#     list.pop(p)
#     a =  0
#     b =  0
#     c =  0
#     for e in range (int(len(list))):
#         if(list[e] == "a"):
#             a+=1
            
#         if(list[e] == "b"):
#             b+=1
            
#         if(list[e] == "c"):
#             c+=1

#     if(a > b):
#         print(f"il reste {b} fois lettre b")
#     elif(b > a):
#         print(f"il reste {a} fois lettre a")
#     else:
#         print(f"il reste {c} fois lettre c")

# remStr(8)

listA = ["1","2","3","4","5"]
listB = ["1","3","5","7","9"]
listC = ["0","2","4","6","8"]

def trList(la,lb):
    for a in range (len(la)):
        
            

trList(listA,listB)
