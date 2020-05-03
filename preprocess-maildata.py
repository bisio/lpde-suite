#!/usr/bin/env python3
import sys
import csv
from shutil import copyfile
from sanitize import sanitize

if len(sys.argv) != 2:
    print("Usage: %s FILE_NAME" % sys.argv[0])
    exit(-1)

filename = sys.argv[1]
copyfile(filename, filename + ".bak")
input_file = open(filename)

input_csv = csv.DictReader(input_file)
rows = list(input_csv)

output_file = open(filename, "w")

processed_rows = []
for row in rows:
    row['first_name'] = sanitize(row['First Name'])
    row['last_name']  = sanitize(row['Last Name'])
    row['FirstName']  = row['First Name']
    row['LastName'] = row['Last Name']
    processed_rows.append(row)

output_csv = csv.DictWriter(output_file, fieldnames=processed_rows[0].keys())
output_csv.writeheader()
for processed_row in processed_rows:
    output_csv.writerow(processed_row)

