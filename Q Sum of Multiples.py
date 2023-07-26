# Link this Example ///   https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python



# Your Job
# Find the sum of all multiples of n below m

# Keep in Mind
# n and m are natural numbers (positive integers)
# m is excluded from the multiples
# Examples
# sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
# sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
# sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
# sumMul(4, -7)  ==> "INVALID"


# My code not correct

# def sum_mul(n, m):
#         num = 0
#         if (n >= 0 and m >= 0):
#             for i in range(n,m+1):
#                 if i % n == 0 :
#                    num+=i
#             return num            
#         else:
#             return("INVALID")
# print(sum_mul(4, 123))    




# my code correct

def sum_mul(start,end):
    sum_of_mul = 0
    if start <= 0 or end <= 0:
        return ("INVALID")  
    else:
        for i in range(start, end,start):
            sum_of_mul += i
        return(sum_of_mul)       
print(sum_mul(2, 9))




# my code correct

# def sum_mul(number, cap):
#     if number <=0 or cap <=0:
#         return("INVALID")
#     multiples = 0
#     sum_of_muliples = 0
#     while multiples < cap:
#         multiples += number
#         if multiples >= cap:
#             break
#         sum_of_muliples+= multiples
#     return (sum_of_muliples)
# print(sum_mul(2, 9)) 