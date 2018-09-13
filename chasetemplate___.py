import microbit
import time
import random
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

# place our block
us = pos.x+1
mc.setBlock(us, pos.y, pos.z, block.DIAMOND_BLOCK)

# start the game by saying Go in the chat
_______SayGo_______
#___DefineStart____

for i in range(15):
    # put challenge block at a random position
    them = random.randint(pos.x-10, pos.x+10)
    mc.setBlock(them, pos.y, pos.z, block.DIRT)
    microbit.display.show(i)

    # wait for user to move their block to the chase block
    while us != them:
        __WaitFor0.1__
        
        # if tilting right, move our block right
        ______________TiltingRight______________
            mc.setBlock(us, pos.y, pos.z, block.AIR)
            us = us + 1
            mc.setBlock(us, pos.y, pos.z, block.DIAMOND_BLOCK)

        # if tilting left, move our block left
        ______________TiltingLeft______________
            mc.setBlock(us, pos.y, pos.z, block.AIR)
            us = us - 1
            mc.setBlock(us, pos.y, pos.z, block.DIAMOND_BLOCK)

# game over
_______Say Game Over_______
microbit.display.show("X")

#___DefineEnd___
#___DefineTimeTaken___
#___SayGameTime=___



