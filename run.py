def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number: "))


if num > 0:
    sign = "positive"
elif num < 0:
    sign = "negative"
else:
    sign = "zero"

if is_prime(num):
    prime_status = "a prime number"
else:
    prime_status = "not a prime number"

print(f"The number is {sign} and {prime_status}.")
5
