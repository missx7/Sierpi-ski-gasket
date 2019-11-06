import numpy as np
import matplotlib.pyplot as plt
import random
point_list = [(0,0),(4,4),(4,0)]
def mid_point (p2):
  p1 = random.choice(point_list)
  return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
m = mid_point(random.choice(point_list))
for i in range(2000):
  m = mid_point(m)
  plt.scatter(m[0],m[1])
plt.show()
