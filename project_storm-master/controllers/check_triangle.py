def is_triangle(x, y, z):        
    if (x + y <= z) or (x + z <= y) or (y + z <= x) : 
        return False
    else: 
        return True    