import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim

x = 1000
t = 1/30

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
for i in range(x):
    time.sleep(t)
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print(i)
p.disconnect()
