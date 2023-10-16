def possible(n, h, healths):
    curr_position = 0
    curr_health = h
    time_elapsed = 0

    while curr_position < n+1 and curr_health > 0:
        next_health = healths[curr_position+1]
        if next_health > 0:
            dummy = curr_position
            count = 1
            while healths[dummy+1] > 0:
                count += 1
                dummy += 1
            print(count)
            if count > 1:
                num_extra_steps = (curr_health-1)//2
                narr = [h_j+time_elapsed+num_extra_steps for h_j in healths[curr_position +
                                                                            1:curr_position+num_extra_steps+1]]
                curr_health -= num_extra_steps*2
                for i, val in enumerate(narr):
                    curr_health += (val+i-1)
                curr_position += count
                time_elapsed += len(narr)+num_extra_steps*2
            else:
                curr_health += (next_health+time_elapsed)-1
                curr_position += 1
                time_elapsed += 1
        else:
            curr_position += 1
            curr_health -= 1
            time_elapsed += 1

    print(curr_position, curr_health, time_elapsed)
    if curr_position == n+1 and curr_health > 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    n_h = input().split(" ")
    healths = input().split(" ")
    n, h = n_h[0], n_h[1]
    n, h = int(n), int(h)
    healths = [int(h) for h in healths]
    print(possible(n, h, healths))
