from abc import ABC, abstractmethod
from typing import List

class UnionFilesInterface(ABC):
    def __init__(self, files_paths : List[str], filename : str) -> None:
        """Union files, union all files in one file

        Args:
            files_paths (List[str]): List with paths to files
            filename (str): Name of file to save

        """        
        raise NotImplementedError()

    def union_files(self) -> None:
        """Union files, union all files in one file

        """        
        raise NotImplementedError()