from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def yes():
  """Don`t forget to download and type in your OWN coordinates!"""
  x = 61
  y = 1
  z = 99
  
  mc.player.setTilePos(x, y, z)

  mc.postToChat("Respawn point set")

answer = input("Continue [Y/n]")
if answer = "y":
  yes()
elif answer = "Y":
  yes()
elif answer = "yes":
  yes()
elif answer = "Yes":
  yes()
elif answer = "YES":
  yes()
