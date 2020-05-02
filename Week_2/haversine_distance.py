import numpy as np

def angular_dist(r1,d1,r2,d2):
  ra1=np.radians(r1)
  ra2=np.radians(r2)
  dec1=np.radians(d1)
  dec2=np.radians(d2)
  
  a=np.sin(np.abs(dec1-dec2)/2)**2
  b=np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
  d=2*np.arcsin(np.sqrt(a + b))
  
  d=np.degrees(d)
  return d
  

if __name__ == '__main__':
  print(angular_dist(21.07, 0.1, 21.15, 8.2))
  print(angular_dist(10.3, -3, 24.3, -29))
