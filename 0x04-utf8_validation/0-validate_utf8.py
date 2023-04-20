#!/usr/bin/python3
"""0-validate_utf8.py"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    if not isinstance(data, list) or not all(isinstance(x, int) for x in data):
        return False

    bytes_remaining = 0
    for byte in data:
        if byte > 255:
            return False
        if bytes_remaining == 0:
            if byte & 0b10000000 == 0:
                continue
            elif byte & 0b11100000 == 0b11000000:
                bytes_remaining = 1
            elif byte & 0b11110000 == 0b11100000:
                bytes_remaining = 2
            elif byte & 0b11111000 == 0b11110000:
                bytes_remaining = 3
            else:
                return False
        else:
            if byte & 0b11000000 != 0b10000000:
                return False
            bytes_remaining -= 1

    return bytes_remaining == 0
