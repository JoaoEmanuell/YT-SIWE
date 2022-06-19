from typing import List

from .interfaces import UnionFilesInterface

class UnionFiles(UnionFilesInterface):
    def __init__(self, files_paths: List[str], filename: str) -> None:
        self.__files_paths = files_paths[::-1] # Reverse the list
        self.__filename = filename

    def union_files(self) -> None:
        classes_functions : List[List[str]] = [] # Context manager, to place
        # containing classes and functions on top of the merged file

        not_classes_functions : List[List[str]] = []

        for file_path in self.__files_paths:

            with open(file_path, 'r') as file:

                file = file.readlines()

                for line in file :

                    if 'function' in line or 'class' in line or '=>' in line:
                        classes_functions.append(
                            self.private__remove_exports_imports(file))
                        break

                # Else in for loop, case this for not break
                
                else : 
                    not_classes_functions.append(
                        self.private__remove_exports_imports(file))

        if classes_functions == [] or not_classes_functions == []:
            classes_functions.append('\n')
            not_classes_functions.append('\n')

        with open(self.__filename, 'w') as file:

            for line in classes_functions:

                file.writelines(line)

            for line in not_classes_functions:

                file.writelines(line)

    def private__remove_exports_imports(self, file : List[str]) -> List[str]:
        new_file : List[str] = []

        for line in file:

            if 'import' in line or 'require' in line:
                pass
            else:
                new_file.append(line.replace('export ', ''))

        return new_file
