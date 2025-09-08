def distance (x1, y1, x2, y2):
    return(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

def main():
    total = distance(55, 12, 180, 74) + distance(3, 5, 3, 2) + distance(9, 6, 12,2)
    print("Total Distance of all three line segments = ",total)        
    main () 