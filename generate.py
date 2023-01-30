import pyrosim.pyrosim as pyrosim
z=0.5
y=0
x=0
l=1
w=1
h=1

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x+1,y+1,z] , size=[l,w,h])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[l,w,h])
    pyrosim.End()

Create_World()
Create_Robot()
