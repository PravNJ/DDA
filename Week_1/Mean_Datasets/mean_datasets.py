import numpy as np

def mean_datasets(file_list):

#Figures out the shape of the array based on the shape of the first file

  shape_test_array=np.loadtxt(file_list[0], delimiter=',')
  data=np.zeros(shape_test_array.shape)

#Reads, then sums values into single numpy array

  for i in range(len(file_list)):
    file_array = np.loadtxt(file_list[i], delimiter=',')
    data+=file_array

#Creates elementwise mean and rounds to one decimal place
  data=np.around(data/float(len(file_list)),decimals=1)
  return(data)

if __name__ == '__main__':
	print(mean_datasets(['data1.csv','data2.csv','data3.csv']))

