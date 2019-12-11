# fibonacci
# good practice is to do both of these inside another function
# don't really want cache to be global
# def fib(n):
#     cache = {} #memorization
#     def fibn(n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         if n not in cache:
#             cache[n] = fibn(n-1) + fibn(n-2)

#         return cache[n]
#     return fibn(n)

def otherway(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    prevprev = 0
    prev = 1

    for _ in range(n-1):
        cur = prevprev + prev
        prevprev = prev
        prev = cur
    return cur
print(otherway(450))



# cache = {} #memorization
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     if n not in cache:
#         cache[n] = fib(n-1) + fib(n-2)

#     return fib(n-1) + fib(n-2)





# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     final = 0
#     for i in range(0, n):
#         final += (i-1) + (i-2) 
#     return final


# for i in range(40):
#     print(fib(i))