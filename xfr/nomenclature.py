
from uuid import UUID, uuid4



class RepositoryID:
    """Uniquely identify a repository"""


    def __init__(self, repository_id:str):
        self.uuid = UUID(str(repository_id)) # UUID converts to str well.


    def __str__(self):
        return str(self.uuid)


    @classmethod
    def create_new(cls):
        return cls(str(uuid4()))




class XrfPath:
    """
    Specifies the path to a file or directory in the Repository.

    Example format:
        xrf://{project_uuid}/{project_path}?branch=feature/new-feature&path=footage/main.mp4
    """


