class DehackedPatchError(Exception):
    """
    Base class for errors in Dehacked file reading/writing.
    """

    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg


class DehackedVersionError(DehackedPatchError):
    """
    Version difference errors in Dehacked file reading.
    """


class DehackedFormatError(DehackedPatchError):
    """
    Patch format version errors in Dehacked file reading.
    """


class DehackedLookupError(DehackedPatchError):
    """
    Patch format key lookup errors in Dehacked file reading.
    """
