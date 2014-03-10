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

#print data['X']

#  we need     (data)  (expected)
#  column two (vol. acidity) (0-2)
#  column 8 density (1)
#  column 11 (alcohol) (5-20)

matrix = np.asmatrix(data['X'])

#  volumetric acidity
pylab.boxplot(matrix[:,1])
pylab.title('Volumetric acidity boxplot (not corrected)')
pylab.ylabel('gdm^-3')
pylab.show()

pylab.hist(matrix[:,1])
pylab.title('histogram volumetric acidity (not corrected)')
pylab.ylabel('frequency')
pylab.xlabel('volumetric acidity (gdm^-3)')
pylab.show()

#  remove outliers
acidity_no_outliers = matrix[:,1][matrix[:,1]<20]

pylab.boxplot(acidity_no_outliers)
pylab.title('volumetric acidity boxplot (outliers removed)')
pylab.ylabel('gdm^-3')
pylab.show()

pylab.hist(acidity_no_outliers.T) #transpose for some weird reason.
pylab.title('Volumetric acidity histogram (outliers removed)')
pylab.xlabel('Volumetric acidity (gdm^-3)')
pylab.ylabel('frequency')
pylab.show()

#  density
pylab.boxplot(matrix[:,7])
pylab.title('Density (not corrected)')
pylab.ylabel('Density (gcm^-3)')
pylab.show()

#  density histogram
pylab.hist(matrix[:,7])
pylab.title('histogram density (not corrected)')
pylab.xlabel('Density (gcm^-3)')
pylab.ylabel('frequency')
pylab.show()

#  remove outliers for density
density_no_outliers = matrix[:,7][matrix[:,7]<1]

#  boxplot
pylab.boxplot(density_no_outliers)
pylab.title('Density (outliers removed)')
pylab.ylabel('Density (gcm^-3)')
pylab.show()

#  density histogram
pylab.hist(density_no_outliers.T)
pylab.title('histogram density (outliers removed)')
pylab.xlabel('Density (gcm^-3)')
pylab.ylabel('frequency')
pylab.show()


#
# Alcohol percentage
#
#  alcohol
pylab.boxplot(matrix[:,10])
pylab.title('alcohol (not corrected)')
pylab.ylabel('alcohol (% vol)')
pylab.show()

#  alcohol histogram
pylab.hist(matrix[:,10])
pylab.title('histogram alcohol (not corrected)')
pylab.xlabel('alcohol (% vol)')
pylab.ylabel('frequency')
pylab.show()

#remove outliers
alcohol_no_outliers = matrix[:,10][matrix[:,10]<200]

#  boxplot
pylab.boxplot(alcohol_no_outliers)
pylab.title('alcohol (outliers removed)')
pylab.ylabel('alcohol (% vol)')
pylab.show()

#  alcohol histogram
pylab.hist(alcohol_no_outliers.T)
pylab.title('histogram alcohol (outliers removed)')
pylab.xlabel('alcohol (% vol)')
pylab.ylabel('frequency')
pylab.show()


# TODO Add comparisons between corrected and non-correcte data.


## 2.1.2


