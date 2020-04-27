from astropy.io import fits
import numpy as np

def mean_fits(file_list):
  data=np.zeros((200,200))
  
  for i in range(len(file_list)):
    hdulist=fits.open(file_list[i])
    fits_array=hdulist[0].data
    data+=fits_array


  data= data/float(len(file_list))
  return(data)

if __name__ == '__main__':
  
  print(mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])[100,100])
  print(mean_fits(['image0.fits', 'image1.fits', 'image3.fits'])[100,100])
  print(mean_fits(['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits'])[100,100])
  