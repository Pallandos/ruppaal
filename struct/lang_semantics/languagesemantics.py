from abc import ABC, abstractmethod

class LanguageSemantics(ABC):

    @abstractmethod
    def initials(self) -> list:
        """Return list of initial states.

        Returns:
            list: List of initial states.
        """
        pass

    @abstractmethod
    def actions(self, state) -> list:
        """Return list of possible actions from a given state.

        Args:
            state (state type): current state

        Returns:
            list: list of possible actions
        """
        pass    

    @abstractmethod
    def execute(self, state, action) -> list:
        """Execute a given action

        Args:
            state (state type): current state
            action (action type): action to execute

        Returns:
            list: list of resulting states
        """
        pass

