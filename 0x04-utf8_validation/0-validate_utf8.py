#!/usr/bin/python3
"""0-validate_utf8.py"""

def validUTF8(data):
    num_bytes = 0

    for i in data:
        if i > 255:
            return False

        if num_bytes == 0:
            if (i >> 7) == 0:
                num_bytes = 1
            elif (i >> 5) == 0b110:
                num_bytes = 2
            elif (i >> 4) == 0b1110:
                num_bytes = 3
            elif (i >> 3) == 0b11110:
                num_bytes = 4
            else:
                return False
        else:
            if (i >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
