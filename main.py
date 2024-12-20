import csv

circuits = open('Harish-Project0/circuits.csv', 'r')
csv_reader = csv.reader(circuits)
for row in csv_reader:
    print(row)