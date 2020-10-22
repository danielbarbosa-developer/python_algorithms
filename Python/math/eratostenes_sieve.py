import math

def prime(number):
    counter = 1
    result = 0

    while(counter <= number):
        if(number%counter == 0):
            result += 1
        counter += 1 
    
    if result == 2:
        return True
    else:
        return False

number_entry = int(input("Enter the final number in the sequence: "))
all_numbers = []
prime_in_limit = []
prime_numbers = []

limit = int(math.sqrt(number_entry) + 1) #The limit of prime numbers to verify

for x in range(number_entry + 1):
    all_numbers.append(x) #Creates a new list with all numbers excluding 0 and 1

for x in range(limit):
    if prime(x):
        prime_in_limit.append(x) #Creates a new list with prime numbers presents in the limit

for prime in prime_in_limit:
    for number in all_numbers:
        if number%prime == 0 and number != prime:
            all_numbers[number] = 0 #All value that isn't prime receive 0
        
for x in all_numbers:
    if all_numbers[x] == 0 or all_numbers[x] == 1:
        continue #Zero values and number 1 are removed
    prime_numbers.append(all_numbers[x])

print(prime_numbers)