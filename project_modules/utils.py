import pandas as pd

'''
Filters given data to a singe departure station

Arguments: 
	- data - Pandas Dataframe object station data
	- d_station_id - int station id

Returns:
	- filtered Pandas Dataframe object
'''
def filter_departure_station(data, d_station_id: int):
    return data[data['Departure station id'] == d_station_id]


'''
Filters given data to a singe return station

Arguments: 
	- data - Pandas Dataframe object station data
	- r_station_id - int station id

Returns:
	- filtered Pandas Dataframe object
'''
def filter_return_station(data, r_station_id: int):
    return data[data['Return station id'] == r_station_id]

'''
Filters data to match a given departure date

Arguments:
    - data - Pandas Dataframe object station data
    - d_date - int weekday

Returns:
    - filtered Pandas Dataframe object
'''
def filter_departure_date(data, d_date: int):
    return data[data['Departure day'] == d_date]