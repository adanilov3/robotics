import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
z=0.5
y=0
x=0
a=1
b=1
c=1

for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[a,b,c])
    z+=1
    a -= (a * 0.1)
    b -= (b * 0.1)
    c -= (c * 0.1)

pyrosim.End()
