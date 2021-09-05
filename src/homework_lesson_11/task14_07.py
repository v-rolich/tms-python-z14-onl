# Дописать скрипт. Программа принимает имя папки и имя
# файла с расширением. Создает папку и создает в ней
# файл. Если расширение файла py - записывает в файл
# код
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dn', '--dir-name',
                    required=True)
parser.add_argument('-fn', '--file-name',
                    required=True)

args = parser.parse_args()
print(args)
os.mkdir(args.dir_name)
os.chdir(args.dir_name)
if 'py' in args.file_name.split('.'):
    with open(args.file_name, 'w') as file:
        file.writelines('''def main():
                                pass
                            if __name__ == '__main__':
                                main()'''
                        )
else:
    a = open(args.file_name, 'w')
