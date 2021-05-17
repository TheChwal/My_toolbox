def factorial(n):
    if n == 0:
        return 1
    if n<0:
        return "Error, negative numbers do not have factorial values!!"
    return n * factorial(n - 1)

def count_down(n):
    print(n)
    if n > 0:
        return count_down(n-1)
    
