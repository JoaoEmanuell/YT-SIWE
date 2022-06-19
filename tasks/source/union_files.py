from typing import List

from .interfaces import UnionFilesInterface

class UnionFiles(UnionFilesInterface):
    def __init__(self, files_paths: List[str], filename: str) -> None:
        self.__files_paths = files_paths
        self.__filename = filename

    def union_files(self) -> None:
        classes_functions : List[List[str]] = [] # Context manager, to place
        # containing classes and functions on top of the merged file

        not_classes_functions : List[List[str]] = []

        union_file : List[str] = [] # Context manager, to place merged file

        for file_path in self.__files_paths:

            with open(file_path, 'r') as file:

                file = file.readlines()

                if 'function' in file or 'class' in file or '=>' in file:
                    classes_functions.append(
                        self.private__remove_exports_imports(file))
                else : 
                    not_classes_functions.append(
                        self.private__remove_exports_imports(file))

        union_file.append(*classes_functions)
        union_file.append(*not_classes_functions)

        with open(self.__filename, 'w') as file:
            file.writelines(union_file)
                
    def private__remove_exports_imports(self, file : List[str]) -> List[str]:
        new_file : List[str] = []

        for line in file:

            if 'import' in line or 'require' in line:
                pass
            else:
                new_file.append(line.replace('export ', ''))

        return new_file