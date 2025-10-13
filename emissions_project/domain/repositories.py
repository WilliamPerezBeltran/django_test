from abc import ABC, abstractmethod

class EmissionRepository(ABC):
    @abstractmethod
    def list(self, filters: dict = None):
        pass
