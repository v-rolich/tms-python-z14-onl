# Дописать скрипт. Программа принимает имя папки и имя
# файла с расширением. Создает папку и создает в ней
# файл. Если расширение файла py - записывает в файл
# следующее:
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-fo', '--folder-name', required=True)
parser.add_argument('-fi', '--file-name', required=True)
args = parser.parse_args()
os.makedirs(args.folder_name)
os.chdir(args.folder_name)
print('Folder name:', args.folder_name)
print('File name:', args.file_name)
with open(args.file_name, 'w') as file:
    if '.py' in args.file_name:
        file.writelines('''def main():
                             pass
                         if __name__ == '__main__':
                            main()'''
                        )
    else:
        file2 = open(args.file_name, 'w')
file.close()
