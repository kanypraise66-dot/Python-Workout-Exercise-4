def hex_output(hexnum):
    decnum = 0
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    return decnum


while True:
    number = input("Enter a hex number (0–9, A–F): ").upper()
    if all(char in "0123456789ABCDEF" for char in number):
        break
    else:
        print("Invalid input. Try again.")

print(hex_output(number))
