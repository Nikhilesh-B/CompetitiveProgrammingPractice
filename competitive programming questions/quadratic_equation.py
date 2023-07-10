import math

# Bondi = "bondi"
# print(Bondi)

# # a=3 
# # b=4 
# # c=5 either ways of this or above is good 

# a,b,c = 684,685,37

# #print(math.cos(2))
# x = a**2+b**2
# y = c**2

# if x == y:
#     print('We have a right triangle!')
# else:
#     print("Boooooo! No right triangle")



# print(a**2+b**2)
# print(c**2)

def is_right_angle_triangle(side1, side2, hypotenuse):
    lhs = side1**2+side2**2
    rhs = hypotenuse**2
    if lhs == rhs: 
        return True
    else:
        return False


print(is_right_angle_triangle(3,4,5))