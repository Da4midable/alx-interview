#!/usr/bin/env python3
"""Module for reading stdin line by line and computing metrics"""

import sys


total_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
line_count = 0


def print_stats():
    """print the stats"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) > 6:
            status_code = parts[-2]
            file_size = parts[-1]

            try:
                total_size += int(file_size)
            except ValueError:
                continue

            if status_code in status_counts:
                status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

finally:
    print_stats()
