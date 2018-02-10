import csv
def loadCSV(filename):
    with open(filename, 'rU') as file:
        data = list(list(rec) for rec in csv.reader(file, delimiter=';'))
    return data