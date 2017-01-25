#!python

import string
number_line = string.digits + string.letters

def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36

    # Decode number

    decoded_num = 0
    # Convert numerical values to base10 values
    list_num = list(str_num)
    for index, value in enumerate(list_num):
        list_num[index] = number_line.index(value)

    # Calculate and Add the value for every digit
    for index, value in enumerate(list_num):
        decoded_num += (base ** (len(list_num) - index - 1)) * int(value)

    return decoded_num


def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36

    # Encode number

    encoded_num = []
    while num:
        # If divisible by base, use 0, else use the remainder
        encoded_num.insert(0, number_line[num % base])
        # Divide number by base
        num /= base
    decodedstring = "".join(encoded_num)
    return decodedstring


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36

    # Convert number
    # decode to base 10
    convert_num = decode(str_num, base1)
    # encode to desired base
    convert_num = encode(convert_num, base2)
    return convert_num

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
