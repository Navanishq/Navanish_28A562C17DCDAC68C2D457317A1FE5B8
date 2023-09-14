def findFact(n):
    if n==1:
        return n
    else:
        return n*findFact(n-1)

print("Enter a Number: ", end="")
try:
    num = int(input())
    fact = findFact(num)
    print("\nFactorial of", num, "=", fact)
except ValueError:
    print("\nInvalid Input!")