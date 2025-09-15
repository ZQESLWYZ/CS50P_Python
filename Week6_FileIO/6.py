import csv

with open("nameandhome.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'],row['Age'])
        
with open("nameandhome.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)