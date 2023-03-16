from abc import ABC, abstractmethod

class Screen(ABC):
    @abstractmethod
    def handle_event(self):
        pass