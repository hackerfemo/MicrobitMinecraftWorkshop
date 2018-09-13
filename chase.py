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

# start the game
mc.postToChat("Go!")
start = time.time()

for i in range(15):
    # put challenge block at a random position
    them = random.randint(pos.x-10, pos.x+10)
    mc.setBlock(them, pos.y, pos.z, block.DIRT)
    microbit.display.show(i)

    # wait for user to move their block to the chase block
    while us != them:
        time.sleep(0.1)
        # if tilting right, move our block right
        if microbit.accelerometer.get_x() > 300:
            mc.setBlock(us, pos.y, pos.z, block.AIR)
            us = us + 1
            mc.setBlock(us, pos.y, pos.z, block.DIAMOND_BLOCK)

        # if tilting left, move our block left
        if microbit.accelerometer.get_x() < -300:
            mc.setBlock(us, pos.y, pos.z, block.AIR)
            us = us - 1
            mc.setBlock(us, pos.y, pos.z, block.DIAMOND_BLOCK)

# game over
mc.postToChat("Game over")
microbit.display.show("X")
end = time.time()
diff = end - start
mc.postToChat("game time=" + str(round(diff)))

