import uuid
from datetime import date, datetime
from enums import Signifier, TaskStatus
from exceptions import EmptyNameError, InvalidStateTransitionError


class Task:
    def __init__(self, name: str, description: str, log_date: date, signifier: Signifier = Signifier.NONE )->None:
        temp_name = name.strip()
        if(temp_name==""):
            raise EmptyNameError("Task cannot be empty")
        self._id: str = str(uuid.uuid4())
        self.name: str = name
        self.description: str = description
        self._creation_date: datetime = datetime.now()
        self.log_date: date = log_date
        self._status: TaskStatus = TaskStatus.TODO
        self.signifier: Signifier = signifier
 
    @property
    def id(self) -> str:
        return self._id

    @property
    def creation_date(self) -> datetime:
        return self._creation_date

    @property
    def status(self) -> str:
        return self._status

    def complete(self) -> None:      # 4 espaces (déclare 'self' pour le 'if' en dessous !)
        if self._status in (         # 8 espaces
            TaskStatus.DONE,
            TaskStatus.CANCELLED,
            TaskStatus.MIGRATED,
        ):
            raise InvalidStateTransitionError("Cannot complete this task.")
        self._status = TaskStatus.DONE

    def cancel(self) -> None:
        if self._status in (TaskStatus.DONE,TaskStatus.MIGRATED):
            raise InvalidStateTransitionError("Cannot cancel this task.")
        self._status = TaskStatus.CANCELLED

    def migrate(self) -> None:
            if self._status != TaskStatus.TODO:
                raise InvalidStateTransitionError("Cannot migrate this task.")
            self._status = TaskStatus.MIGRATED

    def schedule(self) -> None:
            if self._status != TaskStatus.TODO:
                raise InvalidStateTransitionError("Cannot schedule this task.")
            self._status = TaskStatus.SCHEDULED