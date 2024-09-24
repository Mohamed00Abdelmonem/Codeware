def repeat_str(reapter_num, string):

    # return reapter_num * string  
    
    # another way

    result = [string for _ in range(reapter_num) ]
    return ''.join(result)

print(repeat_str(4,'Hello'))     


