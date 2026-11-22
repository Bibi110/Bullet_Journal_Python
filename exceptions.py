class BujoError(Exception):

    pass

class EmptyNameError(BujoError):
    pass

class InvalidStateTransitionError(BujoError):
    pass

class EntryNotFoundError(BujoError):
    pass

class InvalidDateError(BujoError):
    pass