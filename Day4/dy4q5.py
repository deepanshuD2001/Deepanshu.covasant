from itertools import zip_longest

class Poly:
    def __init__(self, *coeffs):
        self.coeffs = list(coeffs)

    def __add__(self, other):
        a = self.coeffs[::-1]  
        b = other.coeffs[::-1]
        summed = [x + y for x, y in zip_longest(a, b, fillvalue=0)]
        return Poly(*summed[::-1])

    def __repr__(self):
        return f"Poly({', '.join(map(str, self.coeffs))})"
        
        
from pkg.poly import Poly

a = Poly(1, 2, 3)  
b = Poly(1, 0, 1, 1, 2, 3) 
c = a + b
print(c) 
        
