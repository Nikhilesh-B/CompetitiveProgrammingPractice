import math


def is_int(n):
    return n - math.floor(n) == 0


if __name__ == "__main__":
    t = int(input())
    radii = []
    for _ in range(t):
        r = int(input())
        radii.append(r)

    for r in radii:
        total_pts = 0
        for x in range(-r, r+1, 1):
            low_y = ((r**2 - x**2)**0.5)
            high_y = (((r+1)**2 - x**2)**0.5)
            is_low_y_int = is_int(low_y)
            is_high_y_int = is_int(high_y)

            if is_low_y_int and is_high_y_int:
                pts = high_y-low_y

            elif is_low_y_int and not is_high_y_int:
                pts = math.floor(high_y) - low_y + 1

            elif not is_low_y_int and is_high_y_int:
                pts = high_y - math.ceil(low_y)
            else:
                pts = math.floor(high_y) - math.ceil(low_y) + 1
            if low_y == 0:
                total_pts += (pts*2)-1
            else:
                total_pts += pts*2
        print(int(total_pts))
