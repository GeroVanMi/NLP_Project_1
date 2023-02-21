import os
from glob import glob

from src.TextFile import TextFile


def read_txt_files_from(directory: str) -> [TextFile]:
    os.chdir(directory)
    file_names = [file for file in glob('*.txt')]

    files = []
    for file_name in file_names:
        files.append(TextFile(file_name))
    return files


def main():
    files = read_txt_files_from('A1004AX2J2HXGL')
    for file in files:
        print(file)


if __name__ == '__main__':
    main()
