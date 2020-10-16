# It converts decimal to binary

decimal_number = int(input("Enter the decimal number: "))

def toBinary(decimal_number):

    operator_number = decimal_number
    binary = 0
    binary_inverted = []

    while(operator_number >= 1):
        if(operator_number == 1):
            binary_inverted.append(operator_number)
            break
        else:
            binary = operator_number%2
            binary_inverted.append(binary)
            operator_number = operator_number//2

    counter = len(binary_inverted) - 1
    binary_string = ""

    while(counter >= 0):
        binary_string += str(binary_inverted[counter])
        counter -=1
    
    return binary_string


print(toBinary(decimal_number)) #Show the binary result as a string
