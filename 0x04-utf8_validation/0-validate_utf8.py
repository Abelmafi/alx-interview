#!/usr/bin/python3
"""0-validate_utf8.py"""

def validUTF8(data):
    n_bytes = 0
    for i in range(8):
        if (data[0] >> (7-i)) & 1:
            n_bytes += 1
        else:
            break

    # Step 2: Check that the remaining bytes start with 10
    if n_bytes == 1 or n_bytes > 4:
        return False
    for i in range(1, n_bytes):
        if i >= len(data):
            return False
        if (data[i] >> 6) != 0b10:
            return False

    # Step 3: Check that the code point is valid
    if n_bytes == 0:
        code_point = data[0]
    else:
        mask = (1 << (n_bytes+1)) - 1
        code_point = data[0] & mask
        for i in range(1, n_bytes):
            code_point = (code_point << 6) | (data[i] & 0b00111111)
    if code_point < 0x80:
        return False
    elif code_point < 0x800:
        return n_bytes == 2
    elif code_point < 0x10000:
        return n_bytes == 3
    elif code_point < 0x110000:
        return n_bytes == 4
    else:
        return False
