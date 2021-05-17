def factorial(n):
    if n == 0:
        return 1
    if n<0:
        return "Error, negative numbers do not have factorial values!!"
    return n * factorial(n - 1)

def count_down(n):
    count=[]
    for i in range(n+1):
        count.append(n-i)
    return count
    
