#! /usr/bin/python2.7

#This will format a MTD turnstile txt file in to a format needed for data
#class project.

import csv
name = '/home/ted/Documents/turnstile_110507.txt'
file = open(name, 'r')
reader = csv.reader(file , delimiter=',')
rows = []
new_rows = []
for row in reader:
    rows.append(row)
file.close()
for row in rows:
    a = row[0]
    b = row[1]
    c = row[2]
    for i in range(3,len(row),5):
        new_rows.append([a, b, c, row[i], row[i+1], row[i+2], row[i+3], row[i+4]])
#TODO need to write to new file named "Updated_"+filename
#for i in range(0,5):
#    print new_rows[i]
new_file = open('/home/ted/Documents/turnstile_110507_update.txt', 'w')
writer = csv.writer(new_file)
writer.writerows(new_rows)
new_file.close

