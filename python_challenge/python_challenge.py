# checks if the number is a prime number
def prime_check(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#stores confirmed prime numbers in an array
def prime_generate(start, end):
    primes = [num for num in range(start, end + 1) if prime_check(num)]
    return primes

# function for file creation and saving
def save_file(primes, file_name):
    with open(file_name, 'w') as file:
        for prime in primes:
            file.write(str(prime) + '\n')

# main program
prime_numbers = prime_generate(1, 250)
FILE_NAME = 'results.txt'

# printing the results
print('Here are the prime numbers between 1 and 250:')
print(prime_numbers)
    
# saving the file
save_file(prime_numbers, FILE_NAME)