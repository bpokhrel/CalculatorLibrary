from __future__ import print_function 
import sys
from flask import Flask
from models.triangle import Triangle
app = Flask(__name__)

@app.route("/")
def hello():
    try:
        tt = Triangle(3,3,3)
    except:
        return "Not a triangle"
    #print("Equilateral triangle",file=sys.stderr)
    return str(tt)
    
