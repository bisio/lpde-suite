#!/usr/bin/env python3

import argparse
import os
import csv
import subprocess
from mailmerge import MailMerge
from sanitize import sanitize

def to_pdf(docx_path):
    subprocess.run(['unoconv','-f', 'pdf', docx_path], cwd=os.path.split(docx_path)[0])

def main(args):
    try:
        os.mkdir(args.output_folder)
    except FileExistsError:
        print("Output folder already exists")

    document = MailMerge(args.template)
    data = csv.DictReader(open(args.data))
    for row in data:
        first_name, last_name = row['First Name'], row['Last Name']
        document.merge(Nome=first_name, Cognome=last_name)
        docx_destination_name = os.path.join(args.output_folder,"%s-%s-%s.docx" % (args.base_name, sanitize(first_name), sanitize(last_name)))
        document.write(docx_destination_name)
        to_pdf(docx_destination_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('lpde-merge')
    parser.add_argument('-t','--template', required=True, dest='template')
    parser.add_argument('-d','--data', required=True, dest='data')
    parser.add_argument('-b','--base-name', required=True, dest='base_name')
    parser.add_argument('-o','--output-folder', required=True, dest='output_folder')

    args = parser.parse_args()
    main(args)
