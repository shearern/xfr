from abc import ABC, abstractmethod
from typing import Dict

class RepositoryStructureError(Exception): pass
class RepositoryOperationError(Exception): pass


class RepositoryStorage(ABC):
    """Interface for reading and writing objects from an XFR repository"""


    @abstractmethod
    def get_repo_metadata(self) -> Dict:
        """Extract metadata from the repository"""


    @abstractmethod
    def write_repo_metadata(self, metadata:Dict):
        """Update metadata in the repository"""


    @classmethod
    def init_repo(cls):
        """Create a new Repository"""
        raise NotImplementedError(f"{cls.__name__}.init_repo() not implemented")


