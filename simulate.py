import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import matplotlib.pylab as plt

x = 1000
t = 1/30

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

backLegJointValues = numpy.zeros(1000)
frontLegJointValues = numpy.zeros(1000)

amplitudeBackLeg = numpy.pi/4
frequencyBackLeg = 1
phaseOffsetBackLeg = 0

amplitudeFrontLeg = -numpy.pi/4
frequencyFrontLeg = 1
phaseOffsetFrontLeg = 0

for i in range(x):
    time.sleep(t)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    backLegPosition = numpy.sin(frequencyBackLeg * x + phaseOffsetBackLeg) *amplitudeBackLeg
    frontLegPosition = numpy.sin(frequencyFrontLeg * x + phaseOffsetFrontLeg) *amplitudeFrontLeg
    backLegJointValues[i] = backLegPosition
    frontLegJointValues[i] = frontLegPosition

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = backLegPosition, maxForce = 100)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = frontLegPosition, maxForce = 100)

p.disconnect()

numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)

numpy.save('data/backLegJointValues.npy', backLegJointValues)
numpy.save('data/frontLegJointValues.npy', frontLegJointValues)
