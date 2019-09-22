from __future__ import print_function 
import sys
from controllers.check_triangle import is_triangle

class Triangle:
    x=None
    y=None
    z=None
     
    def __init__(self, x, y, z):
        self.validate(x,y,z)
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return ("Side 1:"+str(self.x)+", Side 2:"+str(self.y)+", Side 3:"+str(self.z))
    def validate(self,x,y,z):
        if is_triangle(x,y,z)!=True:
            raise ValueError("Not a Triangle")