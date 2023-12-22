import configparser
import os

from ._base import SubCommand, AbortCommand
from ._args import existing_directory

from xfr.profiles import ConfigLoader
from xfr.ask import ask, ask_choose, ask_pass


class InitCommand(SubCommand):


    def __init__(self):
        super().__init__('init', 'Initialize profile file (connect to repo)')
        self.parser.add_argument('--new', action='store_true',
            help="Setup a new repository (default: connect to existing repo)")
        self.parser.add_argument('--home', action='store_true',
            help="Setup profile path in user HOME directory")
        self.parser.add_argument('--path', type=existing_directory, default='.',
            help="Folder to setup profile in")


    def execute(self, args):

        # Determine path to profile to use
        if args.home:
            target = os.path.join(os.path.expanduser('~'), ConfigLoader.PROFILE_FILENAME)
        else:
            target = os.path.join(args.path, ConfigLoader.PROFILE_FILENAME)

        # Prompt for settings
        config = configparser.ConfigParser()
        config.read(target)

        profile_name = ask("Enter the new profile name", default='default')
        if config.has_section(profile_name):
            raise AbortCommand(f"Profile '{profile_name}' already exists int {target}.")
        storage_type = ask_choose("Select storage type",
                                  ['s3', 'local'])

        if storage_type == 's3':
            config[profile_name] = {
                'STORAGE': 's3',
                'BUCKET_NAME': ask("Enter the S3 Bucket Name: "),
                'ACCESS_KEY': ask("Enter the S3 Access Key: "),
                'ACCESS_SECRET': ask_pass("Enter the S3 Access Secret: "),
                'REPOSITORY_PREFIX': ask("Enter the S3 Repository Prefix: "),
                'AWS_REGION': ask("Enter the AWS Region: ")
            }
        elif storage_type == 'local':
            config[profile_name] = {
                'STORAGE': 'local',
                'PATH': ask("Enter the local storage path: ")
            }
        else:
            raise ValueError("Invalid storage type. Must be 's3' or 'local'.")

        # Write out config
        with open(target, 'w') as configfile:
            config.write(configfile)
        print(f"Profile '{profile_name}' written to {target}.")

        storage = 

        # Init Repository
        if args.new:

