# Создать скрипт, который принимает имя фамилию и
# возраст и дописывает их в csv файл
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name',
                    required=True)
parser.add_argument('-ln', '--last-name',
                    required=True)
parser.add_argument('-age', required=True)
args = parser.parse_args()
print(args)

with open('data.csv', 'a') as data:
    data.writelines(f'{args.first_name} {args.last_name} {args.age}\n')
