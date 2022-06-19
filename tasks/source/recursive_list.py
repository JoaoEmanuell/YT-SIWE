from typing import List
from os import listdir
from os.path import isdir, join
from .interfaces import RecursiveListInterface

class RecursiveList(RecursiveListInterface):
    def __init__(self, path: str, file_extension: str = '') -> None:
        self.__path = path
        self.__file_extension = file_extension

    def get_recursive_list(self, paths : List[str] = []) -> List[str]:
        files = listdir(self.__path)

        for file in files :

            if isdir(join(self.__path, file)) :

                paths = RecursiveList(join(self.__path, file), self.__file_extension).get_recursive_list(paths)

            else :
                    
                if self.__file_extension == '' or file.endswith(self.__file_extension) :

                    paths.append(join(self.__path, file))

        return paths