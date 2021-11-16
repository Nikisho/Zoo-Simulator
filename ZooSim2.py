# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:59:22 2021

@author: rphob
"""

import random
from tkinter import *
from tkinter import ttk

class Animal:
    def __init__(self, health):
        self.health = 100
        self.dead = False
        
# =============================================================================
# The function below substracts a random number from the healthl
# =============================================================================
    def healthnegative(self):
        self.health -= random.uniform(0,20)
        if self.health < 0:
            self.health = 0
            
# =============================================================================
# The following classes are used to generate animal objects, with different 
# attributes. A random number is generated for each type of animal
# =============================================================================
class Elephant(Animal): 
    c = random.uniform(10,25)
    def __init__(self, health):
        super().__init__(health)
        self.weak = False
        
    def healthchecker(self):
        if self.weak == True and self.health < 70: #Note: the elephant only dies when it can't walk AND health is < 70
            self.dead = True
            
        elif self.health < 70:
            self.weak = True
            
        elif self.health >= 70:
            self.weak = False
            
class Giraffe(Animal):
    c = random.uniform(10,25)
    def __init__(self, health):
        super().__init__(health)
    def healthchecker(self):
        if self.health < 50:
            self.dead = True

class Monkey(Animal):
    c = random.uniform(10,25)
    def __init__(self, health):
        super().__init__(health)
    def healthchecker(self):
        if self.health < 30:
            self.dead = True
            
# =============================================================================
# The class below contains static methods that will be reused in the buttons. 
# Feed the zoo and go forward in time. The status of each animal is checked and
# printed on the tkinter window.
# =============================================================================
class myzoo():
    def __init__(self, health):
        super().__init__(health)
        
    # The method below goes forward in time. Each time button is pressed, this method is called
    # and the values are updated
    @staticmethod    
    def forward(Array):
        for obj in Array:
            obj.healthnegative()
            obj.healthchecker()   
            
            objtype = Label(root, text=obj.__class__.__name__, padx = 50, pady = 5, bg="#996666")
            objtype.grid(row=Array.index(obj), column=3)
            
            objhealth = Label(root, text= "{:.2f}".format(obj.health), padx = 50, pady = 5, bg="#bfff00")
            objhealth.grid(row=Array.index(obj), column=4)
            
            if obj.dead == True:
                obj.health = 0
                objstatus = Label(root, text = "Dead", padx = 50, pady = 5, bg="#f90606")
                objstatus.grid(row=Array.index(obj),column=5)
            else:
                objstatus = Label(root, text = "Alive", padx = 50, pady = 5, bg="#00bfff")
                objstatus.grid(row=Array.index(obj),column=5)
     
# =============================================================================
# The function below increases the health by a random number between 10 and 25
# =============================================================================    
    @staticmethod                
    def feedthezoo(Array):
        for obj in Array:
            if obj.dead == True:
                pass # Note: we pass if the animal is dead. The health does not increase.
            else:
                obj.health += obj.c #each random valye c corresponds to a class
                if obj.health > 100:
                    obj.health = 100
                objhealth = Label(root, text= "{:.2f}".format(obj.health), padx = 50, pady = 5, bg="#bfff00")
                objhealth.grid(row=Array.index(obj), column=4)
                
            
# =============================================================================
# I create three arrays of five disinct El/Monk/Gi objects with health = 100       
# =============================================================================
El = [1,2,3,4,5]
Gi = [1,2,3,4,5]
Mo = [1,2,3,4,5]
for i in range(5):
    El[i] = Elephant(100)
    Gi[i] = Giraffe(100)
    Mo[i]= Monkey(100)   
    
#Assuming the zoo opens at 10am
hour = 10
def functionhour():
    global hour
    hour +=1 
    if hour == 24:
        hour = 0
    clock = Label(root, text="the time is " + str(hour) +"h00")
    clock.grid(row=3,column=1)
    myzoo.forward(Zoolist)
            
root = Tk()    #defining a tkinter widget
root.geometry("600x500") 
  
Zoolist = Mo+Gi+El #Creating a long list with all the animals that we will then process
def feedme():
    myzoo.feedthezoo(Zoolist)

# =============================================================================
# When we run the code we need a table with the initial values
# =============================================================================
for obj in Zoolist:
    objtype = Label(root, text=obj.__class__.__name__, padx = 50, pady = 5, bg="#996666")
    objtype.grid(row=Zoolist.index(obj), column=3)
    objhealth = Label(root, text="{:.2f}".format(obj.health), padx = 50, pady = 5, bg="#bfff00")
    objhealth.grid(row=Zoolist.index(obj), column=4)
    objstatus = Label(root, text = "Alive", padx = 50, pady = 5, bg="#00bfff")
    objstatus.grid(row=Zoolist.index(obj),column=5)
    
#Initial time on clock
clock = Label(root, text="The time is " + str(hour) +"h00")
clock.grid(row=3,column=1)

#Button to move forward    
plusOnehourbutton = Button(root, text="Plus One hour", padx = 30, pady = 5, command=functionhour)
plusOnehourbutton.grid(row=1, column=1)

#Button to feed the zoo
feedbutton = Button(root, text = "Feed the zoo", padx = 30, pady = 5,  command=feedme)
feedbutton.grid(row=2,column=1)
root.mainloop()


            
    
    
    
        

          
          
  