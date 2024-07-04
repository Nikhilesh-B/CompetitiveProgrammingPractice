import math


def find_open_doors(num_doors):
    open_doors = []

    for door in range(1, num_doors + 1):
        if math.isqrt(door) ** 2 == door:
            open_doors.append(door)

    return open_doors


# Number of doors
num_doors = 100

# Find and print the list of open doors
open_doors = find_open_doors(num_doors)
print(f"Open doors at the end are: {open_doors}")
