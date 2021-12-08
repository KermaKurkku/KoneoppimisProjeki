import pandas as pd

'''
Returns a list of stations from the read DataFrame object

Arguments:
	- data: DataFrame object

Return:
	- List of unique stations
'''
def get_stations(data):
	temp = data['Departure station name'].tolist()
	temp.extend(data['Return station name'].tolist())
	stations = list(set(temp))
	return stations