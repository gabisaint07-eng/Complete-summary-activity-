def distance (x1, y1, x2, y2):
    return(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

distance(55, 12, 180, 74)
distance(3, 5, 3, 2) 
distance(1234, 1, 23, 6)
total = distance(55, 12, 180, 74) + distance(3, 5, 3, 2) + distance(1234, 1, 23, 6)
print("Total Distance of all three line segments = ",total)        