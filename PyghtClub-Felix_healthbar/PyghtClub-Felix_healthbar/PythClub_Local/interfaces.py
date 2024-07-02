from typing import Protocol, runtime_checkable

@runtime_checkable
class IZerstoerbar(Protocol):
    
    def zerstoere(self) -> None:
        raise NotImplementedError
    