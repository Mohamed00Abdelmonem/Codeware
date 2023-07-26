
# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]



def reverse_seq(n):
    result = [(i) for i in range(n, 0,-1)]
    return(result)
    
print(reverse_seq(5))



# def reverse_seq1(n):
#     result = []
#     for i in range(n, 0, -1):
#         result.append(i)
#     return result    


# print(reverse_seq1(5))
   