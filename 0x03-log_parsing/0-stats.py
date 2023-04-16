#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_counts = {code: 0 for code in status_codes}
total_file_size = 0
lines_processed = 0

for line in sys.stdin:
    try:
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        if status_code in status_codes:
            status_code_counts[status_code] += 1
            total_file_size += file_size
        lines_processed += 1
        if lines_processed % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_codes):
                if status_code_counts[code] > 0:
                    print("{}: {}".format(code, status_code_counts[code]))
    except (ValueError, IndexError):
        pass
