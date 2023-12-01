# --- Part Two ---

# Your calculation isn't quite right. It looks like some of the digits are 
# actually spelled out with letters: one, two, three, four, five, six, seven, 
# eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and 
# last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. 
# Adding these together produces 281.

# What is the sum of all of the calibration values?

str_to_digit = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

reversed_str_to_digit = {word[::-1]: digit for word, digit in str_to_digit.items()}


def find_first_spelled_digit(s: str, reversed=False) -> (int, str | None):
    if reversed:
        digit_dict = reversed_str_to_digit
    else:
        digit_dict = str_to_digit

    for j in range(len(s)-3):
        for word in digit_dict.keys():
            # Start to check the first 3 characters in the string, since all the spelled 
            # digits are 3-5 characters long.
            i = s[:3+j].find(word)
            if i >= 0:
                return i, digit_dict[word]
    return -1, None


def find_first_numeric_digit(s: str) -> (int, str | None):
    for i, c in enumerate(s):
        if c.isdigit():
            return i, int(c)
    return -1, None


def get_digit(s: str, reversed=False) -> int:
    i, digit = find_first_numeric_digit(s)
    j, spelled_digit = find_first_spelled_digit(s, reversed=reversed)

    if i == -1:
        return spelled_digit
    elif j == -1:
        return digit
    elif i < j:
        return digit
    else:
        return spelled_digit


def get_number(s: str) -> int:
    return get_digit(s) * 10 + get_digit(s[::-1], reversed=True)


sum = 0
for line in open('input.txt', 'r'):
    sum += get_number(line.strip())

print(sum)
