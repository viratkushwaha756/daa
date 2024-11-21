
def karatsuba(x, y):

    if x < 10 or y < 10:
        return x * y
     
    m = min(len(str(x)), len(str(y)))
    m2 = m // 2

    high1, low1 = divmod(x, 10**m2)
    high2, low2 = divmod(y, 10**m2)
    
    z0 = karatsuba(low1, low2)                
    z1 = karatsuba(low1 + high1, low2 + high2) 
    z2 = karatsuba(high1, high2)               
    
    return z2 * 10**(2 * m2) + (z1 - z2 - z0) * 10**m2 + z0

def square_large_number(number):

    return karatsuba(number, number)

try:
    large_number = int(input("Enter the Number: "))
    result = square_large_number(abs(large_number)) 
    print(f"The square of {large_number} is: {result}")
except ValueError:
    print("Please enter a valid integer.")
