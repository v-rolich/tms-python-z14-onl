"""
Создать скрипт, который принимает имя фамилию и
возраст и дописывает их в csv файл
"""

import argparse as ar
import csv

parser = ar.ArgumentParser()
parser.add_argument('-fn', '--first-name',
                    required=True)
parser.add_argument('-ln', '--last-name',
                    required=True)
parser.add_argument('-a', '--age',
                    required=True)
args = parser.parse_args()
print(args)

lst = [args.first_name, args.last_name, args.age]
with open('File.csv', 'w') as csv_file:
    write = csv.writer(csv_file)
    write.writerow(lst)

print('First name:', args.first_name)
print('Last name:', args.last_name)
print('Age:', args.age)
