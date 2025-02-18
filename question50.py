## LCM: Using the GCD function, write a function lcm(a, b) that returns the least common multiple.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def lcm(a, b):
    return a * b / gcd(a, b)

print(lcm(48, 18))