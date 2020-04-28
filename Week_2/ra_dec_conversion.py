def hms2dec(hours,minutes,seconds):
  dec = 15*(hours + minutes/60 + seconds/(60*60))
  return dec

def dms2dec(degrees,arcminutes,arcseconds):
  if degrees > 0:
    dec = degrees + arcminutes/60 + arcseconds/(60*60)
  elif degrees <0:
    dec = (-1)*((-1)*(degrees) + arcminutes/60 + arcseconds/(60*60))
  return dec
  

if __name__ == '__main__':
  
  print(hms2dec(23, 12, 6))
  print(dms2dec(22, 57, 18))
  print(dms2dec(-66, 5, 5.1))