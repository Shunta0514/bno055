import csv

a = ['a', 'b']

with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(a)
f.close()