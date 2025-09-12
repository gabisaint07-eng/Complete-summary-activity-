#get raduis of polygon
#get the number 0pf sides of the polygon
#calculate the area based on the radius and the number of sides
#return the area  

def traingleArea(base, height):
    return base *height* 0.5 

def polygon_angle(sides):
    return 360/sides 

def triangle_base (hypotenuse, angle):
    return hypotenuse * math.sin(math.radians(angle)) # sine

def triangle_height (hypotenuse, angle):
    return hypotenuse * math.cos(math.radians(angle)) # cosine



def polygon_area(radius, n):
    angle = polygon_angle(n)
    base = triangle_base(radius, angle)
    height =triangle_height(radius, angle)
    tArea: triangleArea(base, height)
    return tArea * n




def main():
     #print("Area of a triangle with base = 4 and height 4 =  " + str(traingleArea(4,4))
     #print("Area of a triangle with base = 4 and height 4 =  ",traingleArea(4,4)
     #print("The angle of the triangles in a polygon with 6 sides is" .polygon_angle(6))
    print("Area of a triangle with base = 4 and height 4 =  ",traingleArea(4,4))
    print("The angle of the triangles in a polygon with 6 sides is", polygon_angle(6))
main() 