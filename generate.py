import pyrosim.pyrosim as pyrosim
z=0.5
y=0
x=0
l=1
w=1
h=1

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[1,1,0.5] , size=[1,1,1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [0.5,0,1])
    pyrosim.Send_Cube(name="Leg", pos=[1,0,1.5], size= [1,1,1])
    pyrosim.End()

Create_World()
Create_Robot()
