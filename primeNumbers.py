# Validate Prime Numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Display Prime Numbers
def display_primes(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")


# Display prime numbers between 1 and 250
display_primes(1, 250)
