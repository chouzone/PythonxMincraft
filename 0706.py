# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:47:06 2021

@author: ruby8
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#陷阱
#取得玩家座標
"""
x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y-1,z+1,x+2,y-1,z-1,206)
mc.setBlock(x+1,y-1,z,11)

mc.setBlocks(x,y,z,x+10,y+20,z+10,95,3)
mc.setBlocks(x+1,y+1,z+1,x+10-1,y+20-1,z+10-1,0)
"""

 
#海綿水壩
x,y,z = mc.player.getTilePos()
a = 0
while a<5:
    mc.setBlocks(x+10,y-30,z,x-10,y+1,z,19)
    z -=5
    a +=1