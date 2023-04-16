#!/usr/bin/env python3
"""..."""
import sys


def print_stats(total_size, status_codes):
    """..."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """..."""
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0
    for line in sys.stdin:
        count += 1
        try:
            parts = line.split()
            size = int(parts[-1])
            status = int(parts[-2])
            total_size += size
            status_codes[status] += 1
        except (ValueError, IndexError):
            continue
        if count % 10 == 0:
            print_stats(total_size, status_codes)
        try:
            sys.stdout.flush()
        except IOError:
            continue
    print_stats(total_size, status_codes)


if __name__ == '__main__':
    main()
