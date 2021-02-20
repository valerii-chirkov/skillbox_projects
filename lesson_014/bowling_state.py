from __future__ import annotations
from abc import ABC, abstractmethod
# from lesson_014.custom_exceptions import ValidSymbolsError, TenFramesError, SlashFirstError, TenPointsFrameError
# from lesson_014.custom_exceptions import OddEvenEqualityError, XAfterNumber

POSSIBLE_SYMBOLS = '123456789-/XХxх'


class Context:
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        Контекст позволяет изменять объект Состояния во время выполнения.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    Контекст делегирует часть своего поведения текущему объекту Состояния.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    Базовый класс Состояния объявляет методы, которые должны реализовать все
    Конкретные Состояния, а также предоставляет обратную ссылку на объект
    Контекст, связанный с Состоянием. Эта обратная ссылка может использоваться
    Состояниями для передачи Контекста другому Состоянию.
    """
    def __init__(self):
        self.operations = {}

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        self.operations = {
            'X': 10,
            '/': lambda x, y: x * y,
            # ...
        }

    @abstractmethod
    def handle2(self) -> None:
        pass


class FirstThrow(State):
    def handle1(self) -> None:
        print("FirstThrow handles request1.")
        print("FirstThrow wants to change the state of the context.")
        self.context.transition_to(SecondThrow())

    def handle2(self) -> None:
        print("FirstThrow handles request2.")


class SecondThrow(State):
    def handle1(self) -> None:
        print("SecondThrow handles request1.")

    def handle2(self) -> None:
        print("SecondThrow handles request2.")
        print("SecondThrow wants to change the state of the context.")
        self.context.transition_to(FirstThrow())


if __name__ == "__main__":
    # Клиентский код.
    context = Context(FirstThrow())
    context.request1()
    context.request2()
    context.request2()
