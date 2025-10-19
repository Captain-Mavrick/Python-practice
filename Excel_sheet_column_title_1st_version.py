Alphabet = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
def convert_to_title(num):
    max_exponent = 0
    while num > 26**max_exponent:
        max_exponent += 1
    while num % 26 == 0 and num > 26:
        test_number = 0
        while test_number * 26**(max_exponent-1) < num:
            test_number += 1 
        print(Alphabet[test_number-1], end = '')
        num = num - (test_number-1) * 26**(max_exponent-1)
        max_exponent -= 1
    while num > 26:
        while (num % 26**(max_exponent-1)) < 26**(max_exponent-2):
            max_exponent -= 1
        leading_number = num // 26**(max_exponent-1)
        print(Alphabet[leading_number], end = '')
        num = num - leading_number * 26**(max_exponent-1)
        max_exponent -= 1  
    print(Alphabet[num], end = ' ')

for i in range(1,101):
    print(f"{i}: ", end = '')
    convert_to_title(i)
