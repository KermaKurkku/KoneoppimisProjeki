import pandas as pd

'''
Filters given data to a singe departure station

Arguments: 
	- data - Pandas Dataframe object
	- d_station_id - int

Returns:
	- filtered Pandas Dataframe object
'''
def filter_departure_station(data, d_station_id: int):
	return data[data['Departure station id'] == d_station_id]

'''
Filters given data to a singe return station

Arguments: 
	- data - Pandas Dataframe object
	- d_station_id - int

Returns:
	- filtered Pandas Dataframe object
'''
def filter_return_station(data, r_station_id: int):
	return data[data['Return station id'] == r_station_id]