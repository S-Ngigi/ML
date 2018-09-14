#!/usr/bin/env python
from math import *
import sys

# Magnitude and angle of vector 1
mag_1 = int(sys.argv[1])
ang_1 = int(sys.argv[2])

# Magnitude and angle of vector 2
mag_2 = int(sys.argv[3])
ang_2 = int(sys.argv[4])


def angle_mag(mag_1, ang_1, mag_2, ang_2):
  """  
  This function is meant to return the magnitude and angle direction
  of the vector derived from adding vectors 1 and 2

  Args:
    mag_1, ang_1 : magnitude and angle of vector 1
    mag_2, ang_2 : magnitude and angle of vector 2
  """
  # Stores the x cordinate for our new vector
  x_component = mag_1*cos(radians(ang_1)) + mag_2*cos(radians(ang_2))
  # Stores the y cordinate for our new vector
  y_component = mag_1*sin(radians(ang_1)) + mag_2*sin(radians(ang_2))

  # Storing the magnitude/ length of our new vector
  new_mag = hypot(x_component, y_component)

  # Stores the angle of our new vector. Note that we begin with y
  new_ang = degrees(atan2(y_component, x_component))

  print(f"It is {isinstance(mag_1, int)}. {mag_1} is a of type {type(mag_1).__name__}.")

  print(f"New magnitude: {new_mag}\nNew angle: {new_ang}")
  

angle_mag(mag_1, ang_1, mag_2, ang_2)