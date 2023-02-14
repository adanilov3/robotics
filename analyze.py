import numpy as numpy
import matplotlib.pyplot

file = numpy.load('data/backLegSensorValues.npy')
file2 = numpy.load('data/frontLegSensorValues.npy')
file3 = numpy.load('data/backLegJointValues.npy')
file4 = numpy.load('data/frontLegJointValues.npy')

backLegSensorValues = numpy.array(file)
frontLegSensorValues = numpy.array(file2)
backLegJointValues = numpy.array(file3)
frontLegJointValues = numpy.array(file4)

matplotlib.pyplot.plot(backLegJointValues, linewidth=2, label='BackLeg')
matplotlib.pyplot.plot(frontLegJointValues, linewidth=2, label='FrontLeg')

#matplotlib.pyplot.plot(backLegSensorValues, label='back leg', linewidth = 2)
#matplotlib.pyplot.plot(frontLegSensorValues, label='front leg')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
