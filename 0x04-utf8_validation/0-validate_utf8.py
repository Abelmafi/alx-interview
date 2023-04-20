#!/usr/bin/python3
"""0-validate_utf8.py"""

def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    num_bytes = 0
    n = len(data)
    for i in range(n):
        if data[i] > 255:
            return False
        if num_bytes == 0:
            if (data[i] >> 7) == 0:
                continue
            elif (data[i] >> 5) == 0b110:
                num_bytes = 2
            elif (data[i] >> 4) == 0b1110:
                num_bytes = 3
            elif (data[i] >> 3) == 0b11110:
                num_bytes = 4
            else:
                return False
        else:
            if (data[i] >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
