runs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
offs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

comb = []
listCombs = []

def recurComb(runsParam):
    global comb
    global listCombs
    for i in offs:
        rr = runsParam[0]
        rr = rr+str(i)
        comb.append(rr)
        if len(runsParam) > 1:
            runsTmp = runsParam[1:].copy() 
            recurComb(runsTmp)
            comb = comb[:-1]
        else:
            listCombs.append(comb)
            if len(listCombs) > 100: #this limits the memory usage. Otherwise, MemoryError for long lists
                print(listCombs)
                listCombs = []
            comb = comb[:-1]
            
            
        
# comb1 = []
# listCombs1 = []
# 
# for i in offs:
#     r = runs[0]
#     r = r+str(i)
#     comb1.append(r)
#     for j in offs:
#         r = runs[1]
#         r = r+str(j)
#         comb1.append(r)
#         for k in offs:
#             r = runs[2]
#             r = r+str(k)
#             comb1.append(r)        
#             for m in offs:
#                 r = runs[3]
#                 r = r+str(m)
#                 comb1.append(r)
#                 listCombs1.append(comb1)
#                 comb1 = comb1[:-1]
#             comb1 = comb1[:-1]
#         comb1 = comb1[:-1]
#     comb1 = comb1[:-1]    
#     
# print(listCombs1)    
# print(len(listCombs1))

# comb = []
# listCombs = []

recurComb(runs)

print(listCombs)    
print(len(listCombs))


    