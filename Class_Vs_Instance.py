"""
Write a Person class with an instance variable, initialAge, and a constructor that takes an integer, initialAge, as a parameter. The
constructor must assign initialAge to age after confirming the argument passed as initialAge is not negative; if a negative
initialAge the constructor should set age to 0 and print Age is not valid, setting age to 0.. 

In addition, you must write the following instance methods:

1. yearPasses() should increase the  instance variable by .
2. amIOld() should perform the following conditional actions:
 if age<13, print you are young..
 if age>= 13 and age<18, print you are teenager..
 Otherwise, print you are old..

"""

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else: 
            self.age = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if(self.age<13): 
            print("You are young.")
        elif(self.age in range(13,18)): 
            print("You are a teenager.")
        else: print("You are old.")     
    def yearPasses(self):
        self.age += 1;

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
