from typing import Protocol, runtime_checkable

@runtime_checkable
class Permanent(Protocol):
    def springen(self) -> None:
        raise NotImplementedError
    
@runtime_checkable
class Temporaer(Protocol):
    def punch(self) -> None:
        raise NotImplementedError