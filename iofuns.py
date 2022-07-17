import csv

def printfcasts(fcasttype, fcasts):
    for fcast in fcasts:
        if type(fcast) == tuple:
            print(fcasttype + " :: " + str(fcast[0]) + " :: " + fcast[1])


def writefcasts(fcasttype, fcasts):
    f = open('fcasts.csv', 'a')
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    for fcast in fcasts:
        row = []
        if type(fcast) != tuple:
            origin_date = fcast
        else:
            row.append(fcast[0].strftime('%Y-%m-%d'))
            row.append(origin_date.strftime('%Y-%m-%d'))
            row.append(fcasttype)
            row.append(fcast[1])
            writer.writerow(row)
    print('Write complete')
    f.close()

def writeactuals(actuals):
    f = open('actuals.csv', 'a')
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(actuals)
    print('Write complete')
    f.close()
