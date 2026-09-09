from dataclasses import dataclass
from typing import Optional

# Dataclasses are used to make classes used for data simpler to maintain and write
@dataclass
class Email:
    id: str
    subject: str
    sender: str
    date: str
    body: Optional[str] = None # To save storage, the body will be a get function rather than the actual text

    def to_dict(self) -> dict:
        return self.__dict__