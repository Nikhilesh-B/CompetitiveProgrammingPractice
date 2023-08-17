import math

val = 0

for i in range(15,22):
    val += math.comb(36,i)*0.7**i*0.3**(36-i)

print("Here the value is", val)