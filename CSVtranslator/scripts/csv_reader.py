import csv

path = '/Users/danielzondberg/Development/Profi/translator/CSVtranslator/assets/'

def read():
    file = open(path + '1.csv')
    reader = csv.reader(file)
    return (reader, file)

print(read())