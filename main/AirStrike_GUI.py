# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:42:04 2024

@author: ASUS
"""
#pip install pygame
import pygame
import AirStrike_Engine



#initialize pygame
pygame.init()

#window caption
pygame.display.set_caption("AirStrike")


#global variable

SQ_SIZE=30 #each cell
H_MARGIN= SQ_SIZE*4 #margin between grid
V_MARGIN= SQ_SIZE #margin between grid
WIDTH= SQ_SIZE*10*2 + H_MARGIN
HEIGHT= SQ_SIZE*10*2 + V_MARGIN
SCREEN= pygame.display.set_mode((WIDTH,HEIGHT))
INDENT=10
GREY=(40,50,60) #Colors
WHITE=(255,250,250) #Colors
GREEN=(50,200,150) #Colors


#function to draw grid

def draw_grid (left = 0,top=0): #top-left specified
    for i in range(100):  #100 cells
    #x,y location of cell (col,row)
        x= left+i % 10 *SQ_SIZE # 10 cols thakbe
        y= top+i // 10 *SQ_SIZE # 10 rows thakbe
        
        #after loacation fixing,draw cell
        square=pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square,width=3)
        



#function to draw ships onto the position grids
def draw_ships(player,left=0,top=0):
    for ship in player.ships:
        x= left+ship.col *SQ_SIZE + INDENT # 10 cols thakbe
        y= top+ship.row  *SQ_SIZE +INDENT # 10 rows thakbe
        if ship.orientation=="h":
            width=ship.size*SQ_SIZE - 2*INDENT
            height=SQ_SIZE - 2*INDENT
        else:
            height=ship.size*SQ_SIZE - 2*INDENT
            width=SQ_SIZE - 2*INDENT
        rectangle=pygame.Rect(x, y, width, height)
        pygame.draw.rect(SCREEN, GREEN, rectangle, border_radius=15)
        #indent jaate ship full cell occupy na kore
        
            
        

player1=AirStrike_Engine.Player()
player2=AirStrike_Engine.Player()

print("player1")
print(player1.indexes)
player1.show_ships()
print("player2")
print(player2.indexes)
player2.show_ships()


#pygame loop
animating = True
pausing = False
while animating:
    #track user interaction
    for event in pygame.event.get():
        
        #user closes pygame window-- Close er code (loop end er)
        if event.type== pygame.QUIT:
            animating = False
            
        #user presses key on keyboard
        if event.type == pygame.KEYDOWN:
            
            #Esc to close animation loop
            if event.key == pygame.K_ESCAPE:
                animating = False
            
            #spacebar to pause/unpause animation
            if event.key == pygame.K_SPACE:
                pausing = not pausing
    
    #execution
    if not pausing:
        
        #draw background
        SCREEN.fill(GREY)
        
        #dray search grids - progress
        draw_grid() # by default 0,0..... player 1
        draw_grid(left= (WIDTH-H_MARGIN)//2+H_MARGIN, top= (HEIGHT-V_MARGIN)//2+V_MARGIN)   #bottom right, player 2
        
        #draw position grids- jekhane ship thakbe
        
        draw_grid(left= (WIDTH-H_MARGIN)//2+H_MARGIN) # top right player 1
        draw_grid(top= (HEIGHT-V_MARGIN)//2+V_MARGIN) #bottom left player 2
        
        
        
        #draw ships
        draw_ships(player2,top= (HEIGHT-V_MARGIN)//2+V_MARGIN)
        draw_ships(player1,left= (WIDTH-H_MARGIN)//2+H_MARGIN)
        
        
        #update screen(otherwise color (grey) , grid etc ta ashbe na)
        
        pygame.display.flip()
        
       #total 4 grid  on screen
       #each player - 2 grids 
       #grid 1 for ship placement
       #grid 2 result and progress


#pygame loop ends here

            
# Quit Pygame properly -- must add just like waitkey in image
pygame.quit()       
            
    