import pathlib
import numpy as np
import csv
from datetime import datetime

date_hour_arr = [
	[0.00, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0,17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23],
	[1.00, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.10, 1.11, 1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.20, 1.21, 1.22, 1.23],
	[2.00, 2.01, 2.02, 2.03, 2.04, 2.05, 2.06, 2.07, 2.08, 2.09, 2.10, 2.11, 2.12, 2.13, 2.14, 2.15, 2.16, 2.17, 2.18, 2.19, 2.20, 2.21, 2.22, 2.23],
	[3.00, 3.01, 3.02, 3.03, 3.04, 3.05, 3.06, 3.07, 3.08, 3.09, 3.10, 3.11, 3.12, 3.13, 3.14, 3.15, 3.16, 3.17, 3.18, 3.19, 3.20, 3.21, 3.22, 3.23],
	[4.00, 4.01, 4.02, 4.03, 4.04, 4.05, 4.06, 4.07, 4.08, 4.09, 4.10, 4.11, 4.12, 4.13, 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21, 4.22, 4.23],
	[5.00, 5.01, 5.02, 5.03, 5.04, 5.05, 5.06, 5.07, 5.08, 5.09, 5.10, 5.11, 5.12, 5.13, 5.14, 5.15, 5.16, 5.17, 5.18, 5.19, 5.20, 5.21, 5.22, 5.23],
	[6.00, 6.01, 6.02, 6.03, 6.04, 6.05, 6.06, 6.07, 6.08, 6.09, 6.10, 6.11, 6.12, 6.13, 6.14, 6.15, 6.16, 6.17, 6.18, 6.19, 6.20, 6.21, 6.22, 6.23]
]

fname = input("Filename: ")

file = open(str(pathlib.Path().resolve())+
	'/Data/od-trips-2020/'+fname, "r")
data_csv = csv.reader(file)
data = list(data_csv)
for i, row in enumerate(data):
	if i == 0:
		continue
	try:
		d_date = datetime.strptime(data[i][0], "%Y-%m-%dT%H:%M:%S")
		r_date = datetime.strptime(data[i][1], "%Y-%m-%dT%H:%M:%S")
		data[i][0] = date_hour_arr[d_date.weekday()][d_date.hour]
		data[i][1] = date_hour_arr[r_date.weekday()][r_date.hour]
	except ValueError:
		print('incorrect row')
		data.remove(row)

file = open(str(pathlib.Path().resolve())+'/Data/'+fname, "w")
writer = csv.writer(file)
writer.writerows(data)
file.close()
#data.to_csv(str(pathlib.Path().resolve())+'/Data/converted/'+fname)
