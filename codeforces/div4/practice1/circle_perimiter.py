import math

if __name__ == "__main__":
    t = int(input())
    radii = []
    for _ in range(t):
        r = int(input())
        radii.append(r)

    for r in radii:
        total_pts = 0
        for x in range(-r, r, 1):
            low_y = ((r**2 - x**2)**0.5)
            high_y = (((r+1)**2 - x**2)**0.5)
            pts = math.floor(high_y-low_y)
            if low_y - math.floor(low_y) == 0:
                pts += 1

            total_pts += pts*2
        print(total_pts)
