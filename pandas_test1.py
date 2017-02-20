import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import cv2

detector = cv2.xfeatures2d.SIFT_create()
style.use('ggplot')
img = cv2.imread(r'D:\Tests\Images\result.jpg')
cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()


