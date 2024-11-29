class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def product_of_digits(num):
            product = 1
            for digit in str(abs(num)):
                product *= int(digit)
            return product
        
        while n > 0:
            if product_of_digits(n) % t == 0:
                return n
            n += 1
            
            
