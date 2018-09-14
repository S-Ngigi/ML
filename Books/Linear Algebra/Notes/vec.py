#!/usr/bin/env python
import sys


def option1(self, a, b):
  print(f"Hi {a} and {b}")

def option2(self, a):
  print(f"Hi {a}")

def option3(self, a, b, c):
  print(f"Hi {a}, {b} and {c}")


options = {
  '1':option1,
  '2':option2,
  '3':option3,
}
option, params = sys.argv[1], sys.argv[1:]
# print(option)
options[option](*params)


