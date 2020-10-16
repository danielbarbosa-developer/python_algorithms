decimal_number = int(input("Enter the decimal number: "))
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
binary_list = []

while(counter >= 0):
    binary_list.append(binary_inverted[counter])
    counter -=1
    

print(binary_list)
