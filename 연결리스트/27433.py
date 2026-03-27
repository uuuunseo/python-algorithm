a = int(input())

# result = 1
# for i in range(1, a+1):
#     result *= i
    
# print(result)

def factorial_loop(a):
    if a == 0: return 1
    else : return a * factorial_loop(a -1)

print(factorial_loop(a))