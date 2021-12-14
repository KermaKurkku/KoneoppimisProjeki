import pathlib
import numpy as np
import pandas as pd
from datetime import datetime


data_types_old = {
	'Departure': str, 'Return': str, 'Departure station id': float, 'Departure station name': str,
	'Return station id': float, 'Return station name': str, 'Covered distance (m)': float, 'Duration (sec.)': int
}
data_types = {
	'Departure': float, 'Return': float, 'Departure station id': int, 'Return station id': int
}

data_types_alt = {
	'Departure day': int, 'Deparure hour': int, 'Return day': int, 'Return hour': int, 'Departure station id': int, 'Return station id': int
}


'''
Reads a csv file using the pandas library
Return:
	- Pandas Dataframe object
'''
def read_data():
	data = pd.read_csv(str(pathlib.Path().resolve())+
		'/Data/station_data.csv', index_col=False, dtype=data_types)
	return data

'''
Reads all stations from a csv file using the pandas library

Return:
	- Pandas Dataframe object
'''
def get_stations():
	stations = pd.read_csv(str(pathlib.Path().resolve())+'/Data/stations.csv', index_col=False)
	stations.drop_duplicates(subset = ["Station name"])
	return stations