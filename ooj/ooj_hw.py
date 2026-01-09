class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1, y1 = map(int, self.coor1)
        x2, y2 = map(int, self.coor2)
        return ((x2-x1)**2 + (y1-y2)**2)**0.5
    
    def slope(self):
        x1, y1 = map(int, self.coor1)
        x2, y2 = map(int, self.coor2)
        return (y2-y1)/(x2-x1)
    
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())


class Cylinder:
    
    global pi
    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (self.height)*(pi)*(self.radius)**2
    
    def surface_area(self):
        return (self.height)*(self.radius)*(pi)*2 + 2*(pi)*(self.radius)**2
    
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())