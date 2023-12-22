
from .nomenclature import RepositoryID
from .storage import RepositoryStorage, RepositoryStructureError


class Repository:
    """Represent a single repository and provide operations"""

    def __init__(self, storage:RepositoryStorage, expected_id:RepositoryID):
        self.storage = storage
        self.__metadata = self.storage.get_repo_metadata()

        try:
            self.__repo_id = self.__metadata['uuid']
        except KeyError:
            raise RepositoryStructureError("Repository metadata missing UUID")

        if expected_id and self.__repo_id != expected_id:
            raise RepositoryStructureError(f"Repository ID mismatch: {self.__repo_id} != {expected_id}")

