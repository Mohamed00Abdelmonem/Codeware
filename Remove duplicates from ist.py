# def distinct(seq):
#     list = []
#     for i in seq:
#         if i > 0:
#             if i not in list:
#                 list.append(i)
#                 list.sort()
#     return list
       
# print(distinct([1,4,3,5,3,-1,-2,4,1]))    



# another selution

def distinct(seq):
    list = []
    for i in seq:
        if i > 0:
            if i not in list:
                list.append(i)
    return list
print(distinct([1,4,3,5,3,-1,-2,4,1]))    
