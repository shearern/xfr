from typing import Dict
import os
import json

from ._base import RepositoryStorage, RepositoryStructureError, RepositoryOperationError
from ..nomenclature import RepositoryID


class LocalRepositoryStorage(RepositoryStorage):
    """Store report files in a local directory"""

    REPOSITORY_METADATA_FILENAME = 'xfr-repository.json'


    def __init__(self, path):
        self.__path = path


    @property
    def root(self):
        return self.__path


    @property
    def metadata_path(self):
        return os.path.join(self.root, self.REPOSITORY_METADATA_FILENAME)


    def get_repo_metadata(self) -> Dict:
        try:
            with open(self.metadata_path, 'r') as fh:
                return json.load(fh)
        except Exception as e:
            raise RepositoryStructureError(f"{e.__class__.__name__}: {e}")


    def write_repo_metadata(self, metadata:Dict):
        with open(self.metadata_path, 'w') as fh:
            json.dump(metadata, fh, indent=4)



    @classmethod
    def init_repo(cls, path, repository_id:RepositoryID=None):
        """Create a new Repository"""

        metadata_path = os.path.join(path, cls.REPOSITORY_METADATA_FILENAME)
        if os.path.exists(metadata_path):
            raise RepositoryOperationError(f"Repository already exists at {path}")

        if repository_id is None:
            repository_id = RepositoryID.create_new()

        with open(metadata_path, 'w') as fh:
            json.dump({'uuid': str(repository_id)}, fh, indent=4)
