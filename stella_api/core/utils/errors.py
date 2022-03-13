class CoreException(Exception):
    """This is the most base exception"""


class FailureLoadVersion(CoreException):
    def __init__(self, version: str) -> None:
        super().__init__(f"Failure to load version {version}")
