from matplotlib import pyplot
import numpy as np
import pandas as pd
import csv
import datetime
import socket

# read actuals into a dict (round the temp to zero decimal digits)
 
actuals_high = {}
actuals_low = {}
fcast = []
fcasts = []

# open actuals file and store highs and lows in separate dicts
# with date as key for each


if socket.gethostname() == "sparta":
    f_act = '/home/johnnie/wxstat/actuals.csv'
else:    
    f_act = 'actuals.csv'

with open(f_act) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        actuals_high[datetime.datetime.strptime(row[1], "%Y-%m-%d")] = row[2]
        actuals_low[datetime.datetime.strptime(row[1], "%Y-%m-%d")] = row[3]

# open fcasts CSV and store rows in list of lists fcasts
        
if socket.gethostname() == "sparta":
    f_fct = '/home/johnnie/wxstat/fcasts.csv'
else:    
    f_fct = 'fcasts.csv'

with open(f_fct) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        fcast.append(datetime.datetime.strptime(row[1],"%Y-%m-%d"))
        fcast.append(datetime.datetime.strptime(row[2],"%Y-%m-%d"))
        fcast.append(row[3])
        fcast.append(row[4])
        fcasts.append(fcast)
        fcast = []

# initialize the data list of lists for each of high and low
# format then the first index key is days between actual and origin of forecast date
# should have a max of difference max_diff

max_diff = 10
data_high = []
data_low = []
for i in range(max_diff):
    data_high.append([])
    data_low.append([])


for row in fcasts:
    if row[2] == "High":
        if row[0] in actuals_high.keys():
            data_high[(row[0]-row[1]).days].append(round(float(row[3]) - \
                                                         float(actuals_high[row[0]]), 2))
    elif row[2] == "Low":
        if row[0] in actuals_low.keys():
            data_low[(row[0]-row[1]).days].append(round(float(row[3]) -
                                                        float(actuals_low[row[0]]), 2))

#for i in range(max_diff):
#    print(i," : HIGH DIFFS : ", data_high[i])
#    print(i," : LOW DIFFS : ", data_low[i])

#print(data_high)
#print(data_low)
    
num_bins = 5
mint = -15
maxt = 15

f, a = pyplot.subplots(4, 1, sharex = True)
f.suptitle('High Diffs')
a = a.ravel()

for idx, ax in enumerate(a):
    ax.set_title(idx)
    ax.hist(data_high[idx], num_bins)

pyplot.xlim([mint,maxt])
pyplot.tight_layout()
pyplot.savefig('/home/johnnie/wxstat/hist_high.png')
print('Saved High Histograms')

f, a = pyplot.subplots(4, 1, sharex = True)
f.suptitle('Low Diffs')
a = a.ravel()

for idx, ax in enumerate(a):
    ax.set_title(idx)
    ax.hist(data_low[idx], num_bins)

pyplot.xlim([mint,maxt])
pyplot.tight_layout()
pyplot.savefig('/home/johnnie/wxstat/hist_low.png')
print('Saved Low Histograms')
