import pybullet as p
import time

x = 1000
t = 1

physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
for i in range(x):
    time.sleep(t)
    p.stepSimulation()
    print(i)
p.disconnect()
