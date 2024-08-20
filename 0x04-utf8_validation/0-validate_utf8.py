#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    # Iterate through the list of integers (bytes)
    i = 0
    while i < len(data):
        # Check the leading bits to determine the character length
        if data[i] & 0b10000000 == 0:  # 1-byte character
            char_length = 1
        elif data[i] & 0b11100000 == 0b11000000:  # 2-byte character
            char_length = 2
        elif data[i] & 0b11110000 == 0b11100000:  # 3-byte character
            char_length = 3
        elif data[i] & 0b11111000 == 0b11110000:  # 4-byte character
            char_length = 4
        else:
            return False  # Invalid leading bits

        # Check if the subsequent bytes follow the continuation pattern
        for j in range(1, char_length):
            if i + j >= len(data) or data[i + j] & 0b11000000 != 0b10000000:
                return False  # Invalid continuation byte

        i += char_length  # Move to the next character

    return True  # All characters are valid
