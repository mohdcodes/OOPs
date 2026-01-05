class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        num, den = self.simplify(self.numerator, self.denominator)
        if den == 1:
            return str(num)
        else:
            return f"{num}/{den}"

    def __add__(self, other):
        temp_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        temp_denominator = self.denominator * other.denominator
        num, den = self.simplify(temp_numerator, temp_denominator)
        return Fraction(num, den)
    
    def __sub__(self, other):
        temp_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        temp_denominator = self.denominator * other.denominator
        num, den = self.simplify(temp_numerator, temp_denominator)
        return Fraction(num, den)
    
    def __mul__(self, other):
        temp_numerator = self.numerator * other.numerator
        temp_denominator = self.denominator * other.denominator
        num, den = self.simplify(temp_numerator, temp_denominator)
        return Fraction(num, den)
    
    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        temp_numerator = self.numerator * other.denominator
        temp_denominator = self.denominator * other.numerator
        num, den = self.simplify(temp_numerator, temp_denominator)
        return Fraction(num, den)

    @staticmethod
    def simplify(numerator, denominator):
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        common_divisor = gcd(abs(numerator), abs(denominator))
        num = numerator // common_divisor
        den = denominator // common_divisor
        # Ensure denominator is positive for standard form
        if den < 0:
            num = -num
            den = -den
        return num, den