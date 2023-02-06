import numpy as numpy
import matplotlib.pyplot

file = numpy.load('data/values.npy')
backLegSensorValues = numpy.array(file)

matplotlib.pyplot.plot(backLegSensorValues)

matplotlib.pyplot.show()

