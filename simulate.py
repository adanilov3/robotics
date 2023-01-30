import pybullet as p
import time

x = 1000
t = 1/30

physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")
for i in range(x):
    time.sleep(t)
    p.stepSimulation()
    print(i)
p.disconnect()
