import csv

with open("test.csv",'w', newline='', encoding='utf-8') as f:
    reader = csv.DictWriter(f, fieldnames=['name', 'age'])
    reader.writerow({'name':'wyz','age':'18'})
    reader.writerow({'name':'1yz','age':'28'})
    reader.writerows([{'name':'1yz','age':'28'}, 
                      {'name':'1yz','age':'28'}]) 