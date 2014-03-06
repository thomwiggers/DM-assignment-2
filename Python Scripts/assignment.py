# -*- coding: utf-8 -*-
"""
Data mining assignment 2

@author: Mats Ouborg (s4118987)
@author: Thom Wiggers (s4119444)
"""
import scipy.io
import pylab 
import numpy as np

data = scipy.io.loadmat('../Data/wine.mat')

print data['X']

# we need     (data)  (expected)
# column two (vol. acidity) (0-2)
# column 8 density (1)
# column 11 (alcohol) (5-20)

matrix = np.asmatrix(data['X'])

#density
pylab.boxplot(matrix[:,1])
pylab.title('Volumetric acidity boxplot (not corrected)')
pylab.xlabel('volumetric acidity')
pylab.ylabel('gdm^-3')
pylab.show()

pylab.hist(matrix[:,1])
pylab.title('histogram volumetric acidity (not corrected)')
pylab.ylabel('frequency')
pylab.xlabel('volumetric acidity')
pylab.show()

# remove outliers
acidity_no_outliers = matrix[:,1][matrix[:,1]<20]

pylab.boxplot(acidity_no_outliers)
pylab.title('volumetric acidity boxplot (outliers removed)')
pylab.xlabel('volumetric acidity')
pylab.ylabel('gdm^-3')
pylab.show()

pylab.hist(acidity_no_outliers.T) #transpose for some weird reason.
pylab.title('Volumetric acidity histogram (outliers removed)')
pylab.xlabel('Volumetric acidity')
pylab.ylabel('frequency')
pylab.show()


# TODO rest of first one.

