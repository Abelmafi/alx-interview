#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8
print(validUTF8([102, 195, 169, 98, 108, 195, 164, 116])) # valid UTF-8 string "féblât"
print(validUTF8([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100])) # valid ASCII string "Hello, World"
print(validUTF8([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 195])) # incomplete last character
print(validUTF8([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 256])) # invalid byte value
print(validUTF8([240, 159, 144, 152]))  # valid 4-byte character: "💀" (unicode U+1F480)
print(validUTF8([240, 159, 144]))# incomplete 4-byte character
print(validUTF8([194, 168])) # incomplete 2-byte character
print(validUTF8([194, 168, 240, 159, 144, 152]))# mixed incomplete characters
print(validUTF8([194, 168, 195, 169])) # mixed complete and incomplete characters

