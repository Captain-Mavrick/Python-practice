Alphabet = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
def convert_to_title(num):
    #Find the max exponent of 26 that is little bit bigger than num
    max_exponent = 0
    while num > 26**max_exponent:
        max_exponent += 1
    #Iteratively find the corresponding alphabet for each exponent, until the number is less than 26
    while num > 26:
        test_number = 0
        while test_number * 26**(max_exponent-1) < num:
            test_number += 1
        if test_number * 26**(max_exponent-1) >= num:
            test_number -= 1
        print(Alphabet[test_number], end = '')
        num = num - (test_number) * 26**(max_exponent-1)
        max_exponent -= 1 
    # The final number value is less than 26 and print its corresponding alphabet
    print(Alphabet[num], end = ' ')

#Some test examples
for i in range(1,101): 
    print(f"{i}:", end = '')
    convert_to_title(i) 