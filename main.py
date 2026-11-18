# question no.1
# main program
import utilities.geometry as g
from utilities.unit_convert import kg_to_pounds
import math 
import random
import datetime as dt

print("rectangle:",g.rectangle(10,5))
print("circle:",g.circle(5))
print("triangle:",g.triangle(10,5))
print("perimeter:"),g.perimeter(10,5)

print("pounds:",kg_to_pounds(5))
print("factorial:",math.factorial(5))


print("random:",random.randint(1,100))


print("time:",dt.datetime.now())