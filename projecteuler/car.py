﻿class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def stop(self):
        print("This car has stopped")

    def drive(self):
        print("This car is driving")