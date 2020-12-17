def square_digits(num):
    output = ""
    for i in str(num):
        output += str(int(i)**2);
    return int(output)

print(square_digits(9119))