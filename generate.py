import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
z=0.5
y=0
x=0
l=1
w=1
h=1

for m in range(5):
    l = 1
    w = 1
    h = 1
    for n in range(5):
        l = 1
        w = 1
        h = 1
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+m,y+n,z+i] , size=[l,w,h])
            l -= (l * 0.1)
            w -= (l * 0.1)
            h -= (l * 0.1)
pyrosim.End()
