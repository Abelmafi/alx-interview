#!/usr/bin/python3
import sys
import signal

# Define a dictionary to store the counts of status codes
status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

# Initialize the total file size
total_file_size = 0

# Define a function to handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    """..."""
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Define a function to print the statistics
def print_stats():
    """..."""
    print(f'Total file size: {total_file_size}')
    for status_code, count in sorted(status_counts.items()):
        if count:
            print(f'{status_code}: {count}')

# Read stdin line by line
for i, line in enumerate(sys.stdin):
    # Parse the line and extract the status code and file size
    try:
        ip, _, _, _, _, status_code, file_size = line.split()
        status_code = status_code.strip()
        file_size = int(file_size.strip())
    except ValueError:
        continue
    
    # Update the status code count and total file size
    if status_code in status_counts:
        status_counts[status_code] += 1
    total_file_size += file_size
    
    # Print the statistics after every 10 lines or keyboard interruption (CTRL + C)
    if (i+1) % 10 == 0:
        print_stats()

# Print the final statistics
print_stats()

