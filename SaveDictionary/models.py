from dataclasses import dataclass
from enum import Enum


class OperationStatus(Enum):
    SUCCESS = "Success"
    FAILURE = "Failure"


@dataclass
class OperationResponse:
    status: OperationStatus
    data: object = None
    error: str = ""
