import math

def get_angles(pos1_x, pos1_y, pos2_x, pos2_y):
    a = pos2_x - pos1_x
    b = pos2_y - pos1_y
    c = math.sqrt(a**2 + b**2)
    alfa = math.degrees(math.asin(a / c))
    beta = math.degrees(math.asin(b / c))
    gama = 90
    return alfa, beta
