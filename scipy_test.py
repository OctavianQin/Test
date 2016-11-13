from numpy import *
import scipy as sp
from pylab import *
import cv2

A = ones((10,5), double)
B = zeros((5,5))

C = sp.randn(10,5)

Cov = transpose(C)*C;