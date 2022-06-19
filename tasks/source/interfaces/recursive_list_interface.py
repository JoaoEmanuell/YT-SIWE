from abc import ABC, abstractmethod
from typing import List

class RecursiveListInterface(ABC):
    def __init__(self, path : str, file_extension : str = '') -> None:
        """Recursive List Interface

        Args:
            path (str): Path to the directory to be listed
            file_extension (str, optional): File extension, list only files 
            with that extension. Defaults to ''.

        """        
        raise NotImplementedError()

    @abstractmethod
    def get_recursive_list(self) -> List[str]:
        """Get recursive list

        Returns:
            List[str]: List with absolute paths to files
        """        
        raise NotImplementedError()