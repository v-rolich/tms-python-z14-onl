# Создать скрипт, который принимает имя фамилию и
# возраст и дописывает их в csv файл

import sys
import argparse
import csv

print(sys.argv)


parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-age', required=True)
args = parser.parse_args()
print(args)

person = [args.first_name, args.last_name, args.age]
with open('task.csv', 'w') as my_file:
    writer = csv.writer(my_file)
    writer.writerow(person)

print('First name:', args.first_name)
print('Last name:', args.last_name)
print('Age:', args.age)
