def Hex_output(Num):
    hex_num = Num
    position = 0
    answer = 0
    for val in hex_num[::-1]:
        hex_decimal = int(val)
        decimal_num = hex_decimal*(16**position)
        position += 1
        answer += decimal_num
    return answer


ref = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16}

while True:
    elements = ['1', '2', '3', '4', '5', '6', '7',
                '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
    number = input("Welcome enter your number:").upper()
    if all(char in elements for char in number):
        break
    else:
        print("Please only enter values 0-9 & A to F")


# for num in number:
#     if num in ref:
#         print(f"{ref[num]}")
#     else:
#         print(f"{num}")

converted_list = [str(ref[char]) if char in ref else (char) for char in number]
print(Hex_output(converted_list))
