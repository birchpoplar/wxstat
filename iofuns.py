import csv
import socket
from datetime import datetime
import datatypes


def printfcasts(fcasts):
    for fcast in fcasts:
        if fcast.bound == "High":
            print(fcast.fcast_date, ' : High : ', fcast.temp)
    for fcast in fcasts:
        if fcast.bound == "Low":
            print(fcast.fcast_date, ' : Low : ', fcast.temp)

            
#        if type(fcast) == tuple:
#            print(fcasttype + " :: " + str(fcast[0]) + " :: " + fcast[1])


def writefcasts(fcasttype, fcasts):

    # need to determine if running on server (assume cronjob)
    if socket.gethostname() == "sparta":
        f = open('/home/johnnie/wxstat/fcasts.csv', 'a')
    else:    
        f = open('fcasts.csv', 'a')

    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    for fcast in fcasts:
        row = []
        if type(fcast) != tuple:
            origin_date = fcast
        else:
            row.append(datetime.now())
            row.append(fcast[0].strftime('%Y-%m-%d'))
            row.append(origin_date.strftime('%Y-%m-%d'))
            row.append(fcasttype)
            row.append(fcast[1])
            writer.writerow(row)
    print(datetime.now(), ': Write complete - fcasts')
    f.close()


def writeactuals(actual):
    row = []
    row.append(datetime.now())
    for item in actual.mk_data_str():
        row.append(item)

    # need to determine if running on server (assume cronjob)
    if socket.gethostname() == "sparta":
        f = open('/home/johnnie/wxstat/actuals.csv', 'a')
    else:    
        f = open('actuals.csv', 'a')

    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(row)
    print(datetime.now(), ': Write complete - actuals')
    f.close()
