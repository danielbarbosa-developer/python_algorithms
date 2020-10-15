#A function that checks whether an input number is prime, returning true or false.

number = int(input("Digite o número: "))

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

print(prime(number))