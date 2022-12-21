#!/usr/bin/env python3

# Created by: Isaiah Fernandez
# Date: December 19, 2022
# This program is the space aliens program on PyBadge.

import ugame
import stage


#This function is the main game game_scene.
def game_scene():
    
    #Image bank for circuit python
    image_background_bank = stage.Bank.from_bmp16("space_aliens_background.bmp")

    #Set background image to zero in the image bank
    #And the size (10x8 of 16x16)
    background = stage.Grid(image_background_bank, 10, 8)

    #Create a stage for the background to show up on
    #And set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    #Set the layers of all sprites
    game.layers = [background]

    #Render all sprites
    #render the background once
    game.render_block()
    
    #Repeat forever, game loop
    while True:
        pass

if __name__ == "__main__":
    game_scene()
