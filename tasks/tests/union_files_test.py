from sys import path
from pathlib import Path
from os.path import join
path.append('../')

from source import RecursiveList, UnionFiles

def test_answer():
    absolute = Path().absolute()
    path = join(absolute, '../', '../', 'siwe', 'src')
    recursive_list = RecursiveList(path, 'js').get_recursive_list()
    UnionFiles(recursive_list, f'{absolute}/tmp.js').union_files()

if __name__ == '__main__':
    test_answer()