from abc import ABC, abstractmethod


class Screen(ABC):
    @abstractmethod
    def handle_event(self, event):
        pass

    @abstractmethod
    def draw(self):
        pass
