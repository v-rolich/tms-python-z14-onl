"""
Создать скрипт, который принимает имя фамилию и
возраст и дописывает их в csv файл
"""

import argparse as ar

parser = ar.ArgumentParser()
parser.add_argument('-fn', '--first-name',
                    required=True)
parser.add_argument('-ln', '--last-name',
                    required=True)
parser.add_argument('-a', '--age', required=True)
args = parser.parse_args()
print(args)

with open('File.csv', 'w') as csv_file:
    csv_file.writelines(f'{args}')
