import numpy as numpy
import matplotlib.pyplot

file = numpy.load('data/backLegSensorValues.npy')
file2 = numpy.load('data/frontLegSensorValues.npy')
file3 = numpy.load('data/backLegAngles.npy')
file4 = numpy.load('data/frontLegAngles.npy')

backLegSensorValues = numpy.array(file)
frontLegSensorValues = numpy.array(file2)
backLegAngles = numpy.array(file3)
frontLegAngles = numpy.array(file4)

matplotlib.pyplot.plot(backLegAngles, linewidth=2, label='BackLeg')
matplotlib.pyplot.plot(frontLegAngles, linewidth=2, label='FrontLeg')

#matplotlib.pyplot.plot(backLegSensorValues, label='back leg', linewidth = 2)
#matplotlib.pyplot.plot(frontLegSensorValues, label='front leg')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
