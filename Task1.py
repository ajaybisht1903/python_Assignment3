#Task 1: Calculate Factorial Using a Function 
n=int(input("Enter the number: " ))
def f(n):
    if n<2:
        return(1)
    else:
        return(n*f(n-1))
result=f(n)
print("Factorial of",n, "is:",result)
