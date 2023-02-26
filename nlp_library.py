import os
from glob import glob

from src.Document import Document


def read_txt_files_from(directory: str) -> [Document]:
    os.chdir(directory)
    file_names = [file for file in glob('*.txt')]

    files = []
    for file_name in file_names:
        files.append(Document(file_name))
    return files


def main():
    files = read_txt_files_from('A1004AX2J2HXGL')
    for file in files:
        print(file)


if __name__ == '__main__':
    main()
