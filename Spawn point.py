from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""Don`t forget to put in your OWN coordinates!"""
x = 61
y = 1
z = 99

mc.player.setTilePos(x, y, z)

mc.postToChat("Client Message: Respawn point set")
