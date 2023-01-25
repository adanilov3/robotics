import pybullet as p
import time

x = 1000
t = 1/60

physicsClient = p.connect(p.GUI)
for i in range(x):
    time.sleep(t)
    p.stepSimulation()
    print(i)
p.disconnect()
