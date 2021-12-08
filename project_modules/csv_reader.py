import pathlib
import pandas as pd

'''
Reads a csv file using the pandas library
Return:
	- Pandas Dataframe object
'''
def read(filename: str):
	data = pd.read_csv(str(pathlib.Path().resolve())+
		'/Data/od-trips-2020/'+filename, index_col=0)
	return data

'''
Reads a csv file using the pandas library and filters it according to the given station number

Return
	- Pandas Dataframe object
'''
def read_and_filter(filename: str, filter: int):
	data = read(filename)
	filter_data = data[data['Departure station id']==filter]
	return filter_data