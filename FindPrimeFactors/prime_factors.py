def find_prime_factors(number):
    prime_factors = []
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1

    return prime_factors


if __name__ == "__main__":
    number = int(input("Enter number: "))
    prime_factors = find_prime_factors(number)
    print(f"The prime factors for {number} are {prime_factors}")
