print("Welcome to the Digital Root Calculator!")
def digitalroot(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
try:
    number = int(input("Enter a non-negative integer to calculate its digital root: "))
    result = digitalroot(number)
    print(f"The digital root of {number} is {result}.")
except ValueError as e:
    print(f"Error: {e}")