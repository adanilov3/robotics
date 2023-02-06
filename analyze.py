import numpy as numpy
import matplotlib.pyplot

file = numpy.load('data/backLegSensorValues.npy')
file2 = numpy.load('data/frontLegSensorValues.npy')

backLegSensorValues = numpy.array(file)
frontLegSensorValues = numpy.array(file2)


matplotlib.pyplot.plot(backLegSensorValues, label='back leg', linewidth = 2)
matplotlib.pyplot.plot(frontLegSensorValues, label='front leg')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
