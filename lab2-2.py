# Author MB 03/04/2022

def build_vehicle(p1, p2, p3, p4):
    wheels = p1
    doors = p2
    axels = p3
    color = p4
    
    return "{0} wheels, {1} doors, {2} axels, {3} color".format(wheels, doors, axels, color)
    
q1 = input("how many wheels: ")
q2 = input("how many doors: ")
q3 = input("how many axels: ")
q4 = input("what color: ")

print(build_vehicle(q1, q2, q3, q4))