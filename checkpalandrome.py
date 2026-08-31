def is_palindrome_math(n: int) -> bool:
    # Negative numbers cannot be palindromes
    if n < 0:
        return False

    original = n
    reversed_num = 0

    while n > 0:
        remainder = n % 10
        reversed_num = (reversed_num * 10) + remainder
        n //= 10

    return original == reversed_num

# Test cases
for val in [121, -121, 10, 1234321]:
    print(f"{val}: {is_palindrome_math(val)}")