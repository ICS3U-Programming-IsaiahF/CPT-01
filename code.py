#!/usr/bin/env python3

# Created by: Isaiah Fernandez
# Date: December 20, 2022
# This program is the space aliens program on PyBadge.

import ugame
import stage


#This function is the main game game_scene.
def game_scene():
    
    #Image banks for circuit python
    image_background_bank = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    #Set background image to 0 in the image bank
    #And the size (10x8 of 16x16)
    background = stage.Grid(image_background_bank, 10, 8)

    #A sprite that will be updated every frame and its location
    ship = stage.Sprite(image_bank_sprites, 8, 75, 66)

    #Create a stage for the background to show up on
    #And set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    #Set the layers of all sprites
    game.layers = [ship] + [background]

    #Render all sprites
    #render the background once
    game.render_block()

    #Repeat forever, game loop
    while True:
        #Get user input

        #Update game logic

        #Redraw Sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
