from sys import path
path.append('../')
from pathlib import Path
from os.path import join

from source import RecursiveList

def test_answer() :
    absolute = Path().absolute()

    path = join(absolute, '../', '../', 'siwe', 'js', '')

    print(path)

    recursive_list_class = RecursiveList(path, '.js')

    recursive_list = recursive_list_class.get_recursive_list()

    assert type(recursive_list) == list

    assert len(recursive_list) == 1

    assert recursive_list == [f'{path}app.js']