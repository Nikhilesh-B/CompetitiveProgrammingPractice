import math
if __name__ == "__main__":
    n_p_k = input().split(" ")
    dose_per_day, max_singled_dose, max_pills = int(n_p_k[0]), int(n_p_k[1]), int(n_p_k[2])
    possible_doses = []


    min_dosage = math.ceil(dose_per_day/max_pills)
    for dose in range(min_dosage, max_singled_dose+1):
        if dose_per_day%dose==0:
            possible_doses.append(dose)

    print(len(possible_doses))
    for dose1 in possible_doses:
        print(dose1)