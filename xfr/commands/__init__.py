
from ._base import XFR_Command, SubCommand

from .add import AddCommand
from .branch import BranchCommand
from .checkout import CheckoutCommand
from .clone import CloneCommand
from .commit import CommitCommand
from .ignore import IgnoreCommand
from .init import InitCommand
from .log import LogCommand
from .merge import MergeCommand
from .pull import PullCommand
from .push import PushCommand
from .status import StatusCommand

# Not sure I like this, but will register all the commands
ADD = AddCommand()
BRANCH = BranchCommand()
CHECKOUT = CheckoutCommand()
CLONE = CloneCommand()
COMMIT = CommitCommand()
IGNORE = IgnoreCommand()
INIT = InitCommand()
LOG = LogCommand()
MERGE = MergeCommand()
PULL = PullCommand()
PUSH = PushCommand()
STATUS = StatusCommand()
