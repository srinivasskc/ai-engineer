class Accumulator:
    def __init__(self) -> None:
        self._count = 0
        # Private Variable as it as _count. (single underscore)
        # This tells, Please do not modify or read _count directly from outside this class
        # -> None:Type hint,Tells this method does not return any data. This constructor job is to setup object, so it always return None.

    @property
    def count(self) -> int:
        return self._count

    # This is for "getter" method.
    # This method is a property. can be used to get the values.

    # Controlled Modification to read-only count with default argument: more=1
    def add(self, more=1) -> None:
        self._count += more