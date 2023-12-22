"""profiles.py - Profiles hold settings for the xfr utility to access the repository"""
import configparser
import os
import getpass
from typing import List


class ProfileConfigError(Exception):
    """Exception raised when expected configuration is missing in a profile."""

    def __init__(self, path, profile, missing_key):
        message = f"Missing '{missing_key}' in the '{profile}' in {path}"
        super().__init__(message)


class ConfigLoader:
    """Find and Load the .xfr.ini file"""

    PROFILE_FILENAME = '.xfr.ini'
    DEFAULT_PROFILE = 'default'


    def __init__(self, profile:str=DEFAULT_PROFILE, path:str=None):
        """
        :param profile: Name of the profile to load
        :param path: If specified, load the config from this path instead of searching for it
        """
        # Find Config
        self.path = path
        if not self.path:
            candidates = self.find_existing_profile_files()
            if len(candidates) == 0:
                raise FileNotFoundError(f"Profile path {path} does not exist")
            self.path = candidates[0]
        if not self.path or not os.path.exists(self.path) or not os.path.isfile(self.path):
            raise FileNotFoundError(f"Could not find {self.PROFILE_FILENAME} file")

        # Parse INI
        self.reader = configparser.ConfigParser()
        self.reader.read(path)

        # Validate config
        self.config = self.validate(profile)


    @classmethod
    def list_possible_profile_paths(cls) -> List[str]:
        # Start in the current directory
        candidates = list()

        path = os.getcwd()
        while True:

            # CWD
            file_path = os.path.join(path, cls.PROFILE_FILENAME)
            candidates.append(file_path)

            # Move up one directory
            new_path = os.path.abspath(os.path.join(path, os.pardir))
            if new_path == path:  # Root directory reached
                break
            path = new_path

        # Check in the user's home directory
        candidates.append(os.path.join(os.path.expanduser('~'), cls.PROFILE_FILENAME))

        return candidates


    @classmethod
    def find_existing_profile_files(cls) -> List[str]:
        paths = list()
        for path in cls.list_possible_profile_paths():
            if os.path.exists(path) and os.path.isfile(path):
                paths.append(path)
        return paths


    def validate(self, profile='default'):
        if profile not in self.config:
            raise ProfileConfigError(profile, 'Profile not found')

        storage_type = self.config[profile].get('STORAGE')
        if not storage_type:
            raise ProfileConfigError(profile, 'STORAGE')

        if storage_type == 's3':
            required_keys = ['BUCKET_NAME', 'ACCESS_KEY', 'ACCESS_SECRET', 'REPOSITORY_PREFIX', 'AWS_REGION']
            missing_keys = [key for key in required_keys if key not in self.config[profile]]
            if missing_keys:
                raise ProfileConfigError(profile, ', '.join(missing_keys))
            return {key: self.config[profile][key] for key in required_keys}

        elif storage_type == 'local':
            if 'PATH' not in self.config[profile]:
                raise ProfileConfigError(profile, 'PATH')
            return {'PATH': self.config[profile]['PATH']}

        else:
            raise ValueError(f"Unknown storage type '{storage_type}'")

