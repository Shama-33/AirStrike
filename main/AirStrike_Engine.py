# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:51:09 2024

@author: ASUS
"""

#import AirStrike_GUI
import random


class Ship:
    def __init__(self,size):
        self.row=random.randrange(0,10)
        self.col=random.randrange(0,10)
        self.size=size
        self.orientation=random.choice(["h","v"])
        self.indexes=self.compute_indexes()  #position determine
    
    def compute_indexes(self):
        start_index=self.row*10 + self.col   
        if self.orientation == "h":
            return [start_index+i for i in range (self.size)]
        elif self.orientation == "v":
            return [start_index+i*10 for i in range (self.size)]
        
'''
s=Ship(size=3)
print(s.row)
print(s.col)
print(s.orientation)
print(s.indexes)
'''

class Player:
    def __init__(self):
        self.ships=[]  #list of planes/ships
        self.search=["U" for i in range(100)]  #search effort - unknown, hit,sunken ship , miss
        #initially shob unknown
        self.place_ships(sizes=[5,4,3,3,2]) #solves out of bound problem   
        list_of_lists=[ship.indexes for ship in self.ships]
        #print(list_of_lists_of_indexes) list_of_lists
        
        #flatten
        self.indexes=[index for sublist in list_of_lists for index in sublist]
        
    def place_ships(self,sizes):
        for size in sizes:
            placed=False
            while not placed:
                #create new ship
                ship = Ship(size)
                #check if placement possible
                possible=True
                for i in ship.indexes:
                    #indexes must be <100 (ver)
                    if i>=100:
                        possible=False
                        break
                    #horizontal out Bound
                    new_row=i//10
                    new_col=i%10
                    if new_row != ship.row and new_col != ship.col:
                        possible=False
                        break
                    #ships cant intersect
                    for other_ship in self.ships:
                        if i in other_ship.indexes:
                            possible=False
                            break
                #place the ship
                if possible:
                    self.ships.append(ship)
                    placed=True
                        
    def show_ships(self):
        indexes=["-" if i not in self.indexes else "X" for i in range (100)]
        for row in range(10):
            print(" ".join(indexes[(row)*10:(row+1)*10]))
                        
                        
'''            
p =Player()
for ship in p.ships:
    print(ship.indexes)  #unpacking jhamela so flatten
'''

'''
p =Player() #list of indexes direct print
print(p.indexes) #flatten done
p.show_ships()
'''
    
                       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        