def reverse(x):
    sign = -1 if x < 0 else 1
    x *= sign
    rev = int(str(x)[::-1])
    return sign * rev if rev < 2**31 else 0

# Example:
print(reverse(-123))  # Output: -321
